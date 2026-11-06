# ccrecover

Recover a dead website from the **Common Crawl** index without depending on
`index.commoncrawl.org` (which is frequently overloaded or down).

The tool talks directly to the data on `data.commoncrawl.org`:

1. reads the per-crawl `cluster.idx` (a SURT key → byte block map),
2. HTTP-range only the compressed CDX blocks that cover your domain,
3. HTTP-range the WARC records listed by the CDX,
4. fills the gaps (pagination, missing pages) and downloads CSS/images from the
   Wayback Machine,
5. writes a browsable mirror and a clean Markdown version of every article.

Only the Python standard library is required. [Pandoc](https://pandoc.org/) is
used for the HTML → Markdown step.

## Why not the official index API?

`index.commoncrawl.org` answers `504 Gateway Time-out` for every query when its
backend is saturated. The legacy 2008–2012 crawls are also incomplete: their
`warc.paths.gz` and `cc-index.paths.gz` files return `404` and the archive
pages warn that they "cannot be comprehensively extracted".

The columnar Parquet index (`s3://commoncrawl/cc-index/table/cc-main/warc/`) is
the documented alternative, but it is not cheap for a single-domain lookup: the
2013 crawl alone has 300 parts of ~571 MB and the Parquet files carry no
zone-map statistics for `url_surtkey` or `url_host_name`. Filtering one domain
means scanning ~170 GB.

`cluster.idx` + HTTP ranges solves the same problem with **megabytes**.

## Install

```bash
git clone https://github.com/cpalau/ccrecover.git
cd ccrecover
chmod +x ccrecover.py
```

Requirements: Python 3.10+, `curl` (optional), `pandoc` for Markdown export.

## Quick start

```bash
# 1. Build a CDX inventory for a domain, filtering by URL substring
./ccrecover.py inventory \
    --domain h-online.com \
    --contains kernel-log \
    --crawl CC-MAIN-2013-48 \
    --out data

# 2. Download the WARC records and write the HTML mirror
./ccrecover.py fetch --records data/records.jsonl --out site

# 3. Fill the pages that Common Crawl missed (pagination, gaps) from Wayback
./ccrecover.py wayback --site site --urls data/missing.txt --out data/records-wayback.jsonl

# 4. Download the original CSS, JS and images from Wayback
./ccrecover.py assets --site site --rate 2

# 5. Convert every article to Markdown
./ccrecover.py markdown \
    --records data/records.jsonl \
    --records data/records-wayback.jsonl \
    --site site --out md

# 6. Build a local index and a coverage report
./ccrecover.py index  --out md --site site
./ccrecover.py report --out md
```

Serve the mirror locally (the pages use root-relative paths):

```bash
cd site && python3 -m http.server 8080
```

## How it works

```text
data.commoncrawl.org
├── cc-index/collections/CC-MAIN-XXXX/
│   └── indexes/cluster.idx        SURT key → (shard, offset, length)
│       └── cdx-00091.gz           independently compressed CDX blocks
└── crawl-data/CC-MAIN-XXXX/
    └── segments/.../*.warc.gz     HTTP range → one WARC record
```

Common Crawl's CDX `.gz` shards are written as **concatenated gzip members**.
Each entry in `cluster.idx` points to a compressed byte range that can be
fetched on its own. For `h-online.com`, the whole domain fits in 76 blocks:
**8.1 MB instead of the 494 MB shard**.

The same trick applies to WARC files: each record is its own gzip member, so
`Range: bytes=offset-(offset+length-1)` returns exactly one record (~15 KB).

## Results: h-online.com Kernel Log

The `recoveries/h-online-kernel-log/` directory contains a full recovery of
The H's *Kernel Log* column (2008–2013):

| Metric | Value |
|---|---|
| Articles | 225 |
| Pages (including pagination) | 398 |
| Words | 327,233 |
| Date range | 2008-02-09 → 2013-06-28 |
| CDX records scanned | 610 |
| CDX blocks downloaded | ~33 MB |
| Mirror size | ~40 MB |
| Sources | Common Crawl CC-MAIN-2013-20/48, 2014-10; Wayback |

See [`recoveries/h-online-kernel-log/README.md`](recoveries/h-online-kernel-log/README.md)
for the full story and the bibliography.

## Reuse it for another site

The tool is domain-agnostic:

```bash
./ccrecover.py inventory --domain example.com --crawl CC-MAIN-2024-10 --out data
```

- `--contains` is optional; without it you get every URL of the domain.
- `--crawl` can be repeated. Use `collinfo.json` to list archives.
- The 2013–2014 crawls are the sweet spot for sites that disappeared around
  then; the monthly crawls from 2013 onwards have complete file listings.
- Older crawls (2008–2012) are not downloadable in full, but their URLs may
  still appear in later crawls if the site survived.

## Legal note

The recovered pages belong to their original publisher. This repository is a
preservation effort: the code is MIT-licensed, the recovered content is kept
for archival and research purposes and will be removed on request from the
rights holder.

## License

MIT. See [LICENSE](LICENSE).
