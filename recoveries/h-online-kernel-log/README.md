# h-online.com — Kernel Log (2008–2013)

Recovered archive of *The H*'s **Kernel Log** column, published by Heise Media
UK between February 2008 and June 2013.

## What is here

| Directory | Contents |
|---|---|
| `md/` | 225 articles in Markdown, one file per article, with YAML front matter |
| `site/` | Browsable mirror: original HTML, CSS, JS and images under their original paths |
| `data/records.jsonl` | 610 CDX records from three Common Crawl crawls |
| `data/records-wayback.jsonl` | 173 pages filled from the Wayback Machine |
| `data/index.json` | Catalog: date, title, author, pages, source URL |
| `md/REPORT.md` | Coverage report by year |

Open `site/index.html` through a local web server:

```bash
cd site && python3 -m http.server 8080
# http://localhost:8080/
```

## Numbers

- **225** articles, **398** pages including pagination.
- **327,233** words, from **2008-02-09** to **2013-06-28**.
- **114** articles by Thorsten Leemhuis, the main author of the column.
- **100** articles span more than one page; the longest, *Linux 2.6.27
  Released*, has 9.
- Common Crawl contributed **222** pages; the Wayback Machine filled **173**
  pagination pages that the crawl missed, plus the CSS and images.

## Why this site

*The H* (`h-online.com`) was an English-language technology publication run by
Heise. Its *Kernel Log* covered Linux kernel development with a level of detail
and continuity that is hard to find today: release candidates, driver changes,
subsystem debates, stable releases. Heise closed the site in 2014 and the
domain now redirects to `heise.de/en`.

The articles were still online in December 2013, so they were captured by
Common Crawl just before the shutdown. The 2008–2009 crawls are not usable
(their file listings return 404), but the 2013 and 2014 crawls contain the
whole site.

## Method (short version)

1. `cluster.idx` maps SURT keys to independently compressed CDX blocks.
   The whole domain is 76 blocks, **8.1 MB** instead of the 494 MB shard.
2. Each CDX record gives `(warc_filename, offset, length)`. A range request
   returns one WARC record, ~15 KB.
3. Pagination pages missing from Common Crawl were fetched from the Wayback
   Machine.
4. CSS, JS and images were fetched from Wayback snapshots around December 2013
   and validated by magic bytes.
5. Pandoc converts the cleaned HTML to Markdown.

The whole pipeline is in [`ccrecover.py`](../../ccrecover.py). The long version,
with diagrams and commands, is the blog post:
<https://cristianpalau.com/resucitar-kernel-log-common-crawl/>.

## Copyright

The articles, images and site design are © Heise Media UK / Heise Medien.
They are reproduced here for preservation, research and personal reading.
No new license is claimed over the recovered content. Rights holders can open
an issue or contact the repository owner to have material removed.
