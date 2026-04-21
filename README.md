# Field Report from the First Hundred Days

**What happened when three founders stopped building software the old way.**

A free, ~40-page field report documenting the methodology that emerged inside [Alchemaize](https://alchemaize.ai) during a hundred-day sprint beginning January 6, 2026. The methodology is called **Continuous Intent Delivery** (CID), and this report is the free precursor to the full-length methodology book, currently in publisher discussions.

**Authors:** David Kim, Casey Robinson, Glenn Knepp
**Status:** Draft v0.1 — April 2026. Not yet final. v1.0 ships alongside the Manning MEAP.
**License:** [CC BY-NC-SA 4.0](LICENSE)

---

## Read it

- **Download the PDF:** [`dist/field-report-v0.pdf`](dist/field-report-v0.pdf)
- **Landing page:** [alchemaize.ai/field-report](https://alchemaize.ai/field-report/)
- **Source (Markdown):** [`FIELD_REPORT_V0.md`](FIELD_REPORT_V0.md)

The PDF is authoritative. The Markdown is the editable source.

## What the report contains

1. **The Shift, in 300 words** — single-page manifesto.
2. **The methodology at working depth** — the five-stage CID loop, the three roles (Intent Engineer / AI Orchestrator / Verification Owner), the Verifiable Outcome Slice (VOS), and the four metrics that replace the velocity dashboard.
3. **The 100-day case study** — 35 production applications, 2 FTE, 3 states. What we counted, what we killed, what we got wrong. The 30× throughput multiplier, claimed conservatively.
4. **One worked VOS** — Casey's cash-flow reconciliation slice on Finaize. Start to finish.
5. **Chapter 1 teaser** — ~3,000 words of *The Shift*, in David's voice.
6. **Chapter 8 excerpts** — Sections 1, 2, and 4 of *Field Report from the Test Pilot* in Casey's voice.
7. **Anticipated questions** — the nine questions we've been asked most often, answered at length.
8. **What this is not / Where to go next** — pointers to the upcoming book.
9. **About the authors + colophon.**

## What the report deliberately doesn't contain

The full methodology — the enterprise layer (ELCID), the compliance-at-generation-time framework, the full adoption path, the anti-patterns chapter, the four appendices — is held for the full-length book. This report is deliberately asymmetric: it gives away the argument and the evidence; it withholds the apparatus. If the argument lands, the book is where the apparatus lives.

## Build the PDF from source

You need [pandoc](https://pandoc.org) and a LaTeX engine (recommended: `xelatex`). On macOS:

```bash
brew install pandoc
brew install --cask mactex-no-gui    # or your preferred TeX distribution
```

Then from the repo root:

```bash
./build.sh
```

The output lands at `dist/field-report-v0.pdf`.

## Contributing

**Typos, grammar, and factual corrections.** Pull requests welcome. Please include the page number or section heading your change targets in the PR description. Small PRs merge faster than big ones.

**Structural feedback, disagreements, questions.** Open an issue rather than a PR. We read all of them; we are actively running the feedback loop between now and the publisher edition.

**Voice edits to the chapter excerpts.** If you want to suggest prose changes to the Chapter 1 or Chapter 8 excerpts, please open an issue first. Those excerpts are pulled from the book-in-progress; changes need to coordinate with the book's editorial process.

## Cite this report

> Kim, D., Robinson, C., & Knepp, G. (2026). *Field Report from the First Hundred Days: What happened when three founders stopped building software the old way* (Draft v0.1). Alchemaize. https://alchemaize.ai/field-report/

BibTeX:

```bibtex
@techreport{alchemaize2026fieldreport,
  title       = {Field Report from the First Hundred Days: What happened when three founders stopped building software the old way},
  author      = {Kim, David and Robinson, Casey and Knepp, Glenn},
  year        = {2026},
  month       = {4},
  note        = {Draft v0.1},
  institution = {Alchemaize},
  url         = {https://alchemaize.ai/field-report/}
}
```

## The book

The full-length methodology book, *Continuous Intent Delivery*, is in publisher discussions as of April 2026. When the MEAP (Manning Early Access Program, or equivalent) launches — targeted late July / early August 2026 — the first three chapters go live. Remaining chapters ship in batches through Q4 2026. Print edition Q1 2027.

To be notified when the MEAP launches, subscribe via [alchemaize.ai/field-report](https://alchemaize.ai/field-report/).

## About Alchemaize

[Alchemaize](https://alchemaize.ai) is a fully distributed studio building AI-native software and teaching the methodology that makes it possible. Founded August 2025 by David Kim and Glenn Knepp; joined by Casey Robinson in October 2025. Brentwood, TN · Claremore, OK · College Station, TX. No office.

Alchemaize is an AWS Partner; the CATALYST consulting engagement launched March 2026.

---

Questions: [team@alchemaize.ai](mailto:team@alchemaize.ai) · [@alchemaize on GitHub](https://github.com/alchemaize)
