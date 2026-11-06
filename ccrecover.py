#!/usr/bin/env python3
"""ccrecover - recover a dead website from the Common Crawl index.

The tool avoids the (often overloaded) Common Crawl index API and works
directly against the data on data.commoncrawl.org:

  1. download the per-crawl `cluster.idx` (a SURT key -> block map),
  2. HTTP-range only the compressed CDX blocks that cover the domain,
  3. HTTP-range the WARC records listed by the CDX,
  4. optionally fill gaps and download assets from the Wayback Machine.

Only the Python standard library is required. Pandoc is used to turn the
recovered HTML into Markdown.

Usage examples:

    ./ccrecover.py inventory --domain h-online.com --contains kernel-log \
        --crawl CC-MAIN-2013-48 --out data

    ./ccrecover.py fetch --records data/records.jsonl --out site

    ./ccrecover.py assets --records data/records.jsonl --out site

    ./ccrecover.py markdown --records data/records.jsonl --out md

    ./ccrecover.py report --records data/records.jsonl --out md
"""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import gzip
import html
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, asdict, field
from pathlib import Path

DATA_BASE = "https://data.commoncrawl.org"
INDEX_BASE = f"{DATA_BASE}/cc-index/collections"
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
WAYBACK = "https://web.archive.org"

# --------------------------------------------------------------------------
# HTTP helpers
# --------------------------------------------------------------------------

_local = threading.local()


def _opener() -> urllib.request.OpenerDirector:
    if not hasattr(_local, "opener"):
        _local.opener = urllib.request.build_opener()
    return _local.opener


def http(
    url: str,
    *,
    headers: dict | None = None,
    byte_range: tuple[int, int] | None = None,
    timeout: int = 90,
    retries: int = 5,
    backoff: float = 2.0,
) -> bytes:
    """GET a URL with retries, optional Range header and browser UA."""
    hdrs = {"User-Agent": UA, "Accept": "*/*"}
    if headers:
        hdrs.update(headers)
    if byte_range:
        hdrs["Range"] = f"bytes={byte_range[0]}-{byte_range[1]}"

    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with _opener().open(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code in (429, 503, 502, 500):
                time.sleep(backoff * (attempt + 1))
                continue
            raise
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last = exc
            time.sleep(backoff * (attempt + 1))
    raise RuntimeError(f"GET failed after {retries} tries: {url}: {last}")


def pool_map(fn, items, workers: int = 8):
    """Run fn over items, yielding (item, result_or_exception)."""
    with futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futs = {pool.submit(fn, item): item for item in items}
        for fut in futures.as_completed(futs):
            item = futs[fut]
            try:
                yield item, fut.result()
            except Exception as exc:  # noqa: BLE001 - reported by caller
                yield item, exc


# --------------------------------------------------------------------------
# CDX inventory via cluster.idx
# --------------------------------------------------------------------------


def surt_prefix(domain: str) -> str:
    """h-online.com -> com,h-online)  (Common Crawl SURT form)."""
    parts = [p for p in domain.lower().split(".") if p]
    return ",".join(reversed(parts)) + ")"


def cluster_index(crawl: str, cache: Path) -> Path:
    cache.mkdir(parents=True, exist_ok=True)
    path = cache / f"cluster-{crawl}.idx"
    if path.exists() and path.stat().st_size > 1_000_000:
        return path
    url = f"{INDEX_BASE}/{crawl}/indexes/cluster.idx"
    print(f"  downloading {crawl} cluster.idx ...", flush=True)
    data = http(url, timeout=300)
    path.write_bytes(data)
    return path


def select_blocks(idx_path: Path, prefix: str) -> list[tuple[str, str, int, int]]:
    """Return (crawl_shard, offset, length) blocks that may contain the prefix."""
    selected: list[tuple[str, str, int, int]] = []
    previous = None
    started = False
    with idx_path.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 5:
                continue
            key = fields[0].split(" ")[0]
            block = (fields[1], int(fields[2]), int(fields[3]))
            if key.startswith(prefix):
                if not started and previous is not None:
                    selected.append(previous)
                started = True
                selected.append(block)
            elif started:
                # The prefix range can continue inside this block even when
                # the block's first key sorts after it: keep it and stop.
                selected.append(block)
                break
            previous = block
    return selected


def parse_cdxj(line: str) -> dict | None:
    line = line.strip()
    if not line or line.startswith("!"):
        return None
    parts = line.split(" ", 2)
    if len(parts) != 3:
        return None
    key, timestamp, payload = parts
    try:
        rec = json.loads(payload)
    except json.JSONDecodeError:
        return None
    rec["surt"] = key
    rec["timestamp"] = timestamp
    return rec


def cmd_inventory(args) -> None:
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    prefix = surt_prefix(args.domain)
    cache = out / "cache"

    all_records: list[dict] = []
    for crawl in args.crawl:
        idx = cluster_index(crawl, cache)
        blocks = select_blocks(idx, prefix)
        total = sum(b[2] for b in blocks)
        print(
            f"{crawl}: {len(blocks)} CDX blocks, {total / 1048576:.1f} MB compressed",
            flush=True,
        )

        def get(block):
            shard, offset, length = block
            url = f"{INDEX_BASE}/{crawl}/indexes/{shard}"
            raw = http(url, byte_range=(offset, offset + length - 1))
            return gzip.decompress(raw).decode("utf-8", "replace")

        found = 0
        for block, text in pool_map(get, blocks, workers=args.workers):
            if isinstance(text, Exception):
                print(f"  ! block failed: {block}: {text}", file=sys.stderr)
                continue
            for line in text.splitlines():
                rec = parse_cdxj(line)
                if not rec:
                    continue
                if not rec.get("surt", "").startswith(prefix):
                    continue
                if args.contains and args.contains.lower() not in rec["url"].lower():
                    continue
                rec["crawl"] = crawl
                all_records.append(rec)
                found += 1
        print(f"{crawl}: {found} matching records", flush=True)

    # Deduplicate: identical URL + digest are the same capture.
    unique: dict[tuple, dict] = {}
    for rec in all_records:
        unique[(rec["url"], rec.get("digest"))] = rec
    records = sorted(unique.values(), key=lambda r: (r["url"], r["timestamp"]))

    path = out / "records.jsonl"
    with path.open("w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"\n{len(records)} unique records -> {path}")


# --------------------------------------------------------------------------
# WARC retrieval
# --------------------------------------------------------------------------


def fetch_record(rec: dict) -> bytes:
    """Fetch and gunzip a single WARC record by byte range."""
    offset = int(rec["offset"])
    length = int(rec["length"])
    url = f"{DATA_BASE}/{rec['filename']}"
    raw = http(url, byte_range=(offset, offset + length - 1), timeout=120)
    return gzip.decompress(raw)


def warc_html(blob: bytes) -> tuple[str, str]:
    """Return (html, content_type) from a WARC response record."""
    # Split WARC headers from the embedded HTTP response.
    try:
        _, rest = blob.split(b"\r\n\r\n", 1)
    except ValueError:
        return blob.decode("utf-8", "replace"), ""
    try:
        http_headers, body = rest.split(b"\r\n\r\n", 1)
    except ValueError:
        return rest.decode("utf-8", "replace"), ""
    head = http_headers.decode("iso-8859-1", "replace")
    ctype = ""
    for line in head.splitlines():
        if line.lower().startswith("content-type:"):
            ctype = line.split(":", 1)[1].strip()
    if body[:2] == b"\x1f\x8b":
        try:
            body = gzip.decompress(body)
        except OSError:
            pass
    return body.decode("utf-8", "replace"), ctype


def asset_path(url: str) -> str:
    """Filesystem path for an asset: query strings are irrelevant on disk."""
    parsed = urllib.parse.urlsplit(url)
    return (parsed.path or "/").lstrip("/")


def url_path(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    path = parsed.path or "/"
    if path.endswith("/"):
        path += "index.html"
    if parsed.query:
        suffix = re.sub(r"[^A-Za-z0-9]+", "-", parsed.query).strip("-")
        base, ext = os.path.splitext(path)
        path = f"{base}__{suffix}{ext}"
    return path.lstrip("/")


def cmd_fetch(args) -> None:
    records = load_records(args.records)
    out = Path(args.out)
    best: dict[str, dict] = {}
    for rec in records:
        if rec.get("status") != "200":
            continue
        key = canonical(rec["url"])
        current = best.get(key)
        if current is None or rec["timestamp"] > current["timestamp"]:
            best[key] = rec

    tasks = []
    for key, rec in best.items():
        dest = out / url_path(rec["url"])
        if dest.exists() and dest.stat().st_size > 200 and not args.force:
            continue
        tasks.append((rec, dest))

    print(f"fetching {len(tasks)} pages ({len(best) - len(tasks)} cached)")

    def work(item):
        rec, dest = item
        blob = fetch_record(rec)
        body, ctype = warc_html(blob)
        if "html" not in ctype and not body.lstrip().lower().startswith("<!doctype"):
            raise ValueError(f"not html ({ctype})")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(body, encoding="utf-8")
        return len(body)

    done = failed = 0
    for (rec, dest), result in pool_map(work, tasks, workers=args.workers):
        if isinstance(result, Exception):
            failed += 1
            print(f"  ! {rec['url']}: {result}", file=sys.stderr)
        else:
            done += 1
            if done % 25 == 0:
                print(f"  {done}/{len(tasks)} pages", flush=True)
    print(f"done: {done} pages, {failed} failed")


# --------------------------------------------------------------------------
# HTML helpers
# --------------------------------------------------------------------------


def canonical(url: str) -> str:
    """Normalise a URL for deduplication."""
    parsed = urllib.parse.urlsplit(url)
    host = parsed.netloc.lower().replace(":80", "")
    path = parsed.path or "/"
    query = parsed.query
    return urllib.parse.urlunsplit(("http", host, path, query, ""))


def strip_tags(fragment: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def find_balanced(html_text: str, start: int, tag: str = "div") -> int:
    """Return the index just after the closing tag matching html_text[start]."""
    depth = 0
    for match in re.finditer(rf"<(/?){tag}\b[^>]*>", html_text[start:]):
        depth += -1 if match.group(1) else 1
        if depth == 0:
            return start + match.end()
    return len(html_text)


@dataclass
class Article:
    url: str
    title: str
    subtitle: str
    author: str
    date: str
    body_html: str
    pages: list[str] = field(default_factory=list)
    next_url: str | None = None


def extract_article(page_html: str, url: str) -> Article:
    title = subtitle = author = date = ""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", page_html, re.S | re.I)
    if m:
        title = strip_tags(m.group(1))
    m = re.search(r"<h2[^>]*>(.*?)</h2>", page_html, re.S | re.I)
    if m:
        subtitle = strip_tags(m.group(1))

    m = re.search(r'<div class="date">(.*?)</div>', page_html, re.S | re.I)
    if m:
        date = strip_tags(m.group(1))
    if not date:
        m = re.search(r'<meta name="date" content="([^"]+)"', page_html, re.I)
        if m:
            date = m.group(1)

    body = ""
    pages: list[str] = []
    nxt = None

    wrapper = re.search(r'<div class="item_wrapper">', page_html)
    if wrapper:
        start = wrapper.end()
        depth = 1
        end = len(page_html)
        for tag in re.finditer(r"<(/?)div\b[^>]*>", page_html[start:]):
            depth += -1 if tag.group(1) else 1
            if depth == 0:
                end = start + tag.start()
                break
        body = page_html[start:end]
        m = re.search(r'href="mailto:[^"]*"\s+title="([^"]+)"', body)
        if m:
            author = html.unescape(m.group(1)).strip()
    else:
        author_end = 0
        m = re.search(r'<h4[^>]*class="author"[^>]*>(.*?)</h4>', page_html, re.S | re.I)
        if m:
            author = re.sub(r"^(?:by|von)\s+", "", strip_tags(m.group(1)), flags=re.I).strip()
            author_end = m.end()
        else:
            m = re.search(r'<div[^>]*class="author"[^>]*>(.*?)</div>', page_html, re.S | re.I)
            if m:
                author = re.sub(r"^(?:by|von)\s+", "", strip_tags(m.group(1)), flags=re.I).strip()
                author_end = m.end()

        if author_end:
            start = author_end
        else:
            m = re.search(r'<p class="page_navi">.*?</p>', page_html, re.S | re.I)
            start = m.end() if m else (page_html.find("<h1") if "<h1" in page_html else 0)

        ends = [
            page_html.find('id="social_bookmarks', start),
            page_html.find('class="feature_option"', start),
            page_html.find('class="related_items"', start),
            page_html.find('id="context_script"', start),
        ]
        ends = [e for e in ends if e != -1]
        end = min(ends) if ends else len(page_html)
        body = page_html[start:end]

    body = re.sub(r"<script.*?</script>", "", body, flags=re.S | re.I)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = re.sub(r'<div class="date">.*?</div>', "", body, flags=re.S | re.I)
    body = re.sub(r'<div class="clear">\s*</div>', "", body, flags=re.S | re.I)
    body = re.sub(r'<div id="social_bookmarks.*?</div>\s*</div>', "", body, flags=re.S | re.I)
    body = re.sub(r'<p class="page_navi">.*?</p>', "", body, flags=re.S | re.I)

    m = re.search(r'<span class="pagination">(.*?)</span>', page_html, re.S | re.I)
    if m:
        for href in re.findall(r'href="([^"]+)"', m.group(1)):
            pages.append(urllib.parse.urljoin(url, html.unescape(href)))

    m = re.search(r'<span class="right"><a href="([^"]+)"[^>]*>\s*next', page_html, re.S | re.I)
    if m:
        nxt = urllib.parse.urljoin(url, html.unescape(m.group(1)))

    return Article(url, title, subtitle, author, date, body, pages, nxt)


def to_markdown(fragment: str) -> str:
    """Clean a mid-2000s HTML fragment and convert it to GitHub Markdown.

    The archived pages are full of unclosed divs and presentational spans;
    pandoc falls back to raw HTML when it meets them. Unwrapping those tags
    and dropping attributes GFM cannot express keeps the output portable.
    """
    fragment = re.sub(r"<(script|style|noscript|iframe)\b.*?</\1>", "", fragment, flags=re.S | re.I)
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    fragment = re.sub(r"</?(div|span)\b[^>]*>", "", fragment, flags=re.I)

    def clean_tag(match: re.Match) -> str:
        tag = match.group(0)
        if tag.lower().startswith("<a"):
            keep = ("href", "title")
        else:
            keep = ("src", "alt", "title")
        tag = re.sub(
            r'\s+([a-zA-Z-]+)="[^"]*"',
            lambda m: m.group(0) if m.group(1).lower() in keep else "",
            tag,
        )
        return tag

    fragment = re.sub(r"<(?:a|img)\b[^>]*>", clean_tag, fragment, flags=re.I)
    fragment = re.sub(r'\s+(?:style|class|align|valign|bgcolor)="[^"]*"', "", fragment, flags=re.I)
    fragment = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.I)

    pandoc = shutil.which("pandoc")
    if not pandoc:
        return strip_tags(fragment)
    proc = subprocess.run(
        [pandoc, "-f", "html", "-t", "gfm", "--wrap=none"],
        input=fragment,
        text=True,
        capture_output=True,
        check=False,
    )
    md = proc.stdout.strip()
    md = re.sub(r'<img[^>]*src="data:[^"]*"[^>]*>', "", md, flags=re.I)
    md = re.sub(r"</?(div|span)\b[^>]*>", "", md, flags=re.I)
    md = re.sub(r"\n{3,}", "\n\n", md)
    # Make local links and images work when the Markdown lives next to site/.
    md = re.sub(r"\]\((/(?!/)[^)]+)\)", r"](../site\1)", md)
    return md.strip()


MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11,
    "december": 12,
}


def iso_date(text: str) -> str:
    """'10 October 2008, 08:38' -> '2008-10-10'."""
    m = re.search(r"^(\d{4})-(\d{2})-(\d{2})", text)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.search(r"(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})", text)
    if not m:
        return ""
    day, month, year = m.group(1), m.group(2).lower(), m.group(3)
    num = MONTHS.get(month)
    return f"{year}-{num:02d}-{int(day):02d}" if num else ""


# --------------------------------------------------------------------------
# Markdown export
# --------------------------------------------------------------------------


def load_records(path: str | Path) -> list[dict]:
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def cmd_markdown(args) -> None:
    records = []
    for path in args.records:
        records.extend(load_records(path))
    site = Path(args.site)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    articles = []
    for rec in records:
        if rec.get("status") != "200":
            continue
        path = site / url_path(rec["url"])
        if not path.exists():
            continue
        page = path.read_text(encoding="utf-8", errors="replace")
        art = extract_article(page, rec["url"])
        art.pages = [p for p in art.pages if canonical(p) != canonical(rec["url"])]
        articles.append(art)

    # Merge pagination: a page is a continuation when another article links to it.
    by_url = {canonical(a.url): a for a in articles}
    continuations = set()
    for art in articles:
        for link in art.pages:
            key = canonical(link)
            if key in by_url:
                continuations.add(key)

    sections: dict[str, list[Article]] = {}
    for art in articles:
        key = canonical(art.url)
        if key in continuations:
            continue
        chain = [art]
        seen = {key}
        for link in art.pages:
            nxt = canonical(link)
            if nxt in seen or nxt not in by_url:
                continue
            seen.add(nxt)
            chain.append(by_url[nxt])
        sections[key] = chain

    rows = []
    for key, chain in sorted(sections.items(), key=lambda kv: iso_date(kv[1][0].date)):
        first = chain[0]
        date = iso_date(first.date)
        slug = re.sub(r"[^a-z0-9]+", "-", first.title.lower()).strip("-")[:80]
        slug = slug or re.sub(r"[^a-z0-9]+", "-", key)[:60]
        name = f"{date or 'undated'}-{slug}.md"
        dest = out / name

        body_parts = []
        for page in chain:
            md = to_markdown(page.body_html)
            if md and md not in body_parts:
                body_parts.append(md)

        front = [
            "---",
            f'title: "{first.title.replace(chr(34), chr(39))}"',
            f"date: {date}" if date else "date:",
            f'author: "{first.author}"' if first.author else "author:",
            f"source: {first.url}",
            f"pages: {len(chain)}",
            "---",
            "",
            f"# {first.title}",
            "",
        ]
        if first.subtitle:
            front += [f"*{first.subtitle}*", ""]
        if first.author:
            front += [f"**{first.author}**", ""]
        text = "\n".join(front) + "\n" + "\n\n".join(body_parts) + "\n"
        dest.write_text(text, encoding="utf-8")

        rows.append(
            {
                "date": date,
                "title": first.title,
                "author": first.author,
                "pages": len(chain),
                "url": first.url,
                "chars": len(text),
                "file": name,
            }
        )

    (out / "index.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(rows)} articles -> {out}")


def cmd_index(args) -> None:
    """Build a local index.html for the recovered mirror."""
    rows = json.loads((Path(args.out) / "index.json").read_text(encoding="utf-8"))
    by_year: dict[str, list[dict]] = {}
    for row in rows:
        by_year.setdefault((row["date"] or "0000")[:4], []).append(row)

    parts = [
        "<!DOCTYPE html>",
        '<html lang="en"><head><meta charset="utf-8">',
        "<title>Kernel Log archive - The H</title>",
        '<link rel="stylesheet" href="/styles/standard.css">',
        "<style>body{background:#fff;color:#222;max-width:900px;margin:2rem auto;padding:0 1rem;font-family:Helvetica,Arial,sans-serif}"
        "h1{font-size:1.6rem}ul{line-height:1.5}.year{margin-top:2rem;font-weight:bold;font-size:1.2rem}"
        "small{color:#666}</style></head><body>",
        "<h1>Kernel Log &mdash; The H (h-online.com)</h1>",
        f"<p><small>{len(rows)} recovered articles, 2008&ndash;2013. "
        "Original text and images: Heise Media UK. Recovered from the Common Crawl and the Wayback Machine.</small></p>",
    ]
    for year in sorted(by_year):
        parts.append(f'<div class="year">{year}</div><ul>')
        for row in sorted(by_year[year], key=lambda r: r["date"]):
            path = urllib.parse.urlsplit(row["url"]).path
            parts.append(
                f'<li><small>{row["date"]}</small> <a href="{path}">{html.escape(row["title"])}</a> '
                f'<small>&mdash; {html.escape(row["author"] or "The H")}</small></li>'
            )
        parts.append("</ul>")
    parts.append("</body></html>")
    (Path(args.site) / "index.html").write_text("\n".join(parts), encoding="utf-8")
    print(f"index -> {Path(args.site) / 'index.html'}")


# --------------------------------------------------------------------------
# Assets (Wayback)
# --------------------------------------------------------------------------


ASSET_RE = re.compile(
    r'(?:href|src)="((?:https?://[^/"]+)?/[^"]+?\.'
    r'(?:css|js|png|jpe?g|gif|ico|svg|woff2?|ttf|eot)(?:\?[^"]*)?)"',
    re.I,
)


def collect_assets(site: Path, host: str = "www.h-online.com") -> set[str]:
    found: set[str] = set()
    for path in site.rglob("*.html"):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for match in ASSET_RE.finditer(text):
            url = urllib.parse.urlsplit(match.group(1))
            if url.path.startswith("/") and not url.path.startswith("//") and not url.path.startswith("/_static/"):
                found.add(urllib.parse.urlunsplit(("http", host, url.path, url.query, "")))
    return found


class Throttle:
    def __init__(self, per_second: float):
        self.min_interval = 1.0 / per_second
        self.lock = threading.Lock()
        self.last = 0.0

    def wait(self):
        with self.lock:
            delta = time.time() - self.last
            if delta < self.min_interval:
                time.sleep(self.min_interval - delta)
            self.last = time.time()


def wayback_snapshot(url: str, preferred: str = "20131215") -> str | None:
    """Return the timestamp of a usable Wayback snapshot for a URL."""
    query = urllib.parse.urlencode(
        {
            "url": url,
            "output": "json",
            "fl": "timestamp,mimetype,statuscode",
            "filter": "statuscode:200",
            "from": "2012",
            "to": "2016",
            "limit": "8",
        }
    )
    try:
        raw = http(
            f"{WAYBACK}/cdx/search/cdx?{query}",
            headers={"Accept": "application/json"},
            timeout=60,
            retries=4,
            backoff=5.0,
        )
    except Exception:
        return None
    try:
        rows = json.loads(raw)
    except json.JSONDecodeError:
        return None
    if len(rows) < 2:
        return None
    best = None
    best_delta = None
    for row in rows[1:]:
        ts = row[0]
        delta = abs(int(ts[:8]) - int(preferred))
        if best_delta is None or delta < best_delta:
            best, best_delta = ts, delta
    return best


def valid_asset(url: str, data: bytes) -> bool:
    """Reject Wayback HTML error pages saved under an asset extension."""
    ext = os.path.splitext(urllib.parse.urlsplit(url).path)[1].lower()
    head = data[:200].lstrip().lower()
    if head.startswith(b"<!doctype") or head.startswith(b"<html"):
        return False
    if ext == ".png":
        return data[:8] == b"\x89PNG\r\n\x1a\n"
    if ext in (".jpg", ".jpeg"):
        return data[:2] == b"\xff\xd8"
    if ext == ".gif":
        return data[:3] == b"GIF"
    if ext == ".ico":
        return data[:4] in (b"\x00\x00\x01\x00", b"\x00\x00\x02\x00")
    if ext == ".svg":
        return b"<svg" in data[:2000].lower()
    return True


def cmd_assets(args) -> None:
    site = Path(args.site)
    assets = collect_assets(site, args.host)
    print(f"{len(assets)} unique assets referenced")
    throttle = Throttle(args.rate)
    missing: list[str] = []
    done = 0

    def work(url):
        dest = site / asset_path(url)
        if dest.exists() and dest.stat().st_size > 0 and not getattr(args, "force", False):
            return "cached"
        throttle.wait()
        ts = args.timestamp
        if args.lookup:
            ts = wayback_snapshot(url, preferred=ts[:8]) or ts
        endpoint = f"{WAYBACK}/web/{ts}/{url}"
        data = http(
            endpoint,
            headers={"Referer": "https://www.h-online.com/", "Accept": "*/*"},
            timeout=60,
            retries=4,
            backoff=8.0,
        )
        if not valid_asset(url, data):
            raise RuntimeError("not an archived asset")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        return "ok"

    ok = cached = failed = 0
    for url, result in pool_map(work, sorted(assets), workers=args.workers):
        done += 1
        if isinstance(result, Exception):
            failed += 1
            missing.append(url)
            print(f"  ! {url}: {result}", file=sys.stderr)
        elif result == "cached":
            cached += 1
        else:
            ok += 1
            if done % 20 == 0:
                print(f"  {done}/{len(assets)} assets", flush=True)
    (site.parent / "data" / "missing-assets.txt").write_text("\n".join(missing) + "\n", encoding="utf-8")
    print(f"assets: {ok} downloaded, {cached} cached, {failed} missing")


# --------------------------------------------------------------------------
# Wayback gap filling
# --------------------------------------------------------------------------

PAGE_QUERY_RE = re.compile(r'(href)="([^"]*?)(\?page=(\d+))"')


def cmd_wayback(args) -> None:
    """Fetch URLs missing from Common Crawl from the Wayback Machine."""
    site = Path(args.site)
    urls = [line.strip() for line in Path(args.urls).read_text(encoding="utf-8").splitlines() if line.strip()]
    records = []
    throttle = Throttle(args.rate)

    def work(url):
        dest = site / url_path(url)
        if dest.exists() and dest.stat().st_size > 500 and not args.force:
            return "cached"
        throttle.wait()
        endpoint = f"{WAYBACK}/web/{args.timestamp}/{url}"
        data = http(
            endpoint,
            headers={"Referer": "https://www.h-online.com/"},
            timeout=90,
            retries=6,
            backoff=15.0,
        )
        if b"suspected abusive bot" in data or len(data) < 500:
            raise RuntimeError("wayback throttle")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        return "ok"

    ok = cached = failed = 0
    for url, result in pool_map(work, urls, workers=args.workers):
        if isinstance(result, Exception):
            failed += 1
            print(f"  ! {url}: {result}", file=sys.stderr)
        elif result == "cached":
            cached += 1
        else:
            ok += 1
        records.append({"url": url, "status": "200", "source": "wayback", "timestamp": args.timestamp})

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(json.dumps(r) for r in records) + "\n", encoding="utf-8")
    print(f"wayback: {ok} downloaded, {cached} cached, {failed} failed -> {out}")


def cmd_relink(args) -> None:
    """Rewrite ?page=N links so the local mirror resolves them."""
    site = Path(args.site)
    count = 0
    for path in site.rglob("*.html"):
        text = path.read_text(encoding="utf-8", errors="replace")
        new = PAGE_QUERY_RE.sub(lambda m: f'{m.group(1)}="{m.group(2)}__page-{m.group(4)}.html"', text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            count += 1
    print(f"relinked {count} pages")


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------


def cmd_report(args) -> None:
    rows = json.loads((Path(args.out) / "index.json").read_text(encoding="utf-8"))
    by_year: dict[str, int] = {}
    for row in rows:
        year = (row["date"] or "sin fecha")[:4]
        by_year[year] = by_year.get(year, 0) + 1
    lines = ["# Informe de recuperación", "", f"Artículos: **{len(rows)}**", "", "| Año | Artículos |", "|---|---|"]
    for year in sorted(by_year):
        lines.append(f"| {year} | {by_year[year]} |")
    lines += [
        "",
        f"Palabras totales (aprox.): {sum(r['chars'] for r in rows) // 6:,}",
        "",
        "## Artículos",
        "",
        "| Fecha | Título | Páginas |",
        "|---|---|---|",
    ]
    for row in sorted(rows, key=lambda r: r["date"]):
        lines.append(f"| {row['date']} | {row['title']} | {row['pages']} |")
    (Path(args.out) / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"report -> {Path(args.out) / 'REPORT.md'}")


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("inventory", help="build a CDX inventory from cluster.idx")
    p.add_argument("--domain", required=True)
    p.add_argument("--crawl", action="append", required=True)
    p.add_argument("--contains", help="only keep URLs containing this substring")
    p.add_argument("--out", default="data")
    p.add_argument("--workers", type=int, default=8)
    p.set_defaults(func=cmd_inventory)

    p = sub.add_parser("fetch", help="download WARC records and write HTML")
    p.add_argument("--records", required=True)
    p.add_argument("--out", default="site")
    p.add_argument("--workers", type=int, default=8)
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_fetch)

    p = sub.add_parser("assets", help="download CSS/JS/images from the Wayback Machine")
    p.add_argument("--site", default="site")
    p.add_argument("--host", default="www.h-online.com")
    p.add_argument("--timestamp", default="20131215000000")
    p.add_argument("--rate", type=float, default=1.5, help="requests per second")
    p.add_argument("--workers", type=int, default=2)
    p.add_argument("--lookup", action="store_true", help="resolve each asset through the CDX API first (slow)")
    p.set_defaults(func=cmd_assets)

    p = sub.add_parser("markdown", help="convert recovered pages to Markdown")
    p.add_argument("--records", required=True, action="append")
    p.add_argument("--site", default="site")
    p.add_argument("--out", default="md")
    p.set_defaults(func=cmd_markdown)

    p = sub.add_parser("wayback", help="fill URLs missing from Common Crawl")
    p.add_argument("--site", default="site")
    p.add_argument("--urls", required=True)
    p.add_argument("--timestamp", default="20131215000000")
    p.add_argument("--out", default="data/records-wayback.jsonl")
    p.add_argument("--rate", type=float, default=1.5)
    p.add_argument("--workers", type=int, default=2)
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_wayback)

    p = sub.add_parser("index", help="build a local index.html for the mirror")
    p.add_argument("--out", default="md")
    p.add_argument("--site", default="site")
    p.set_defaults(func=cmd_index)

    p = sub.add_parser("relink", help="rewrite ?page=N links to local files")
    p.add_argument("--site", default="site")
    p.set_defaults(func=cmd_relink)

    p = sub.add_parser("report", help="write a coverage report")
    p.add_argument("--out", default="md")
    p.set_defaults(func=cmd_report)

    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
