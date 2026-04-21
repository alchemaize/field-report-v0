# Leanpub manuscript folder

This folder is the Leanpub GitHub Writing Mode source. Leanpub generates
the Leanpub edition of the report by pulling from this folder, not from
the root of the repo.

## How it works

Leanpub reads two files to decide what goes into the book and what goes
into the free sample:

- `Book.txt` lists every file that appears in the book, in order.
- `Sample.txt` lists files that appear in the free sample.

Each `.md` file in this folder is a chapter (in Leanpub's vocabulary).
The field report's nine Parts are eleven files here (cover, about, nine
Parts, colophon), kept separate so Leanpub paginates cleanly between them.

## Syntax

Files use Leanpub-Flavored Markdown, which is close enough to the pandoc
source that they compile in both toolchains without modification. Two
deltas to know:

1. No `\newpage` directives. Leanpub paginates automatically between
   files listed in `Book.txt`, so page breaks are controlled by the file
   split, not by inline directives.
2. No YAML frontmatter. Title, author, and publication metadata are set
   in Leanpub's web settings (Book Settings -> Metadata), not in the
   markdown.

Everything else (headings, code fences, emphasis, lists, blockquotes)
is identical to the pandoc source.

## How to sync

1. Push commits to the repo on GitHub.
2. In Leanpub, open the book's Writing page and click "Preview" or
   "Publish." Leanpub pulls from `manuscript/` on the default branch.
3. Check the generated PDF/EPUB previews before publishing.

## Keeping this folder in sync with the authoritative source

The authoritative source is `FIELD_REPORT_V0.md` in the repo root. To
regenerate this folder after editing the authoritative source, run:

```bash
python3 scripts/split-for-leanpub.py
```

(That script is in `scripts/split-for-leanpub.py` alongside the build
script. It reads the root source, strips YAML frontmatter, splits on
`\newpage` directives, and writes per-Part files here.)

## Files

- `00-cover.md` - title page
- `01-about.md` - About this document
- `02-part-01-manifesto.md` - Part I. The Manifesto
- `03-part-02-how-cid-works.md` - Part II. How CID Works
- `04-part-03-case-study.md` - Part III. The Case Study
- `05-part-04-worked-vos.md` - Part IV. One Worked VOS
- `06-part-05-chapter-1-teaser.md` - Part V. Chapter 1 Teaser
- `07-part-06-chapter-8-excerpts.md` - Part VI. Chapter 8 Excerpts
- `08-part-07-anticipated-questions.md` - Part VII. Anticipated Questions
- `09-part-08-not-and-next.md` - Part VIII. What This Is Not
- `10-part-09-authors.md` - Part IX. About the Authors
- `11-colophon.md` - Colophon

## Free sample

The free sample (controlled by `Sample.txt`) includes the cover, the
about page, Part I (manifesto), and Part II (how CID works). That's
roughly the first 12 pages of the report. It's the argument, without
the evidence.
