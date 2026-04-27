#!/usr/bin/env python3
"""
Split FIELD_REPORT_V0.md into per-Part files for the Leanpub manuscript/
folder. Run from the repo root.

The authoritative source is FIELD_REPORT_V0.md. This script derives the
Leanpub edition from it so the two stay in sync.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "FIELD_REPORT_V0.md")
OUT = os.path.join(ROOT, "manuscript")

FILENAME_MAP = [
    ("cover",              "00-cover.md"),
    ("about",              "01-about.md"),
    ("part-i-",            "02-part-01-manifesto.md"),
    ("part-ii-",           "03-part-02-how-cid-works.md"),
    ("part-iii-",          "04-part-03-case-study.md"),
    ("part-iv-",           "05-part-04-worked-vos.md"),
    ("part-v-",            "06-part-05-chapter-1-teaser.md"),
    ("part-vi-",           "07-part-06-chapter-8-excerpts.md"),
    ("part-vii-",          "08-part-07-anticipated-questions.md"),
    ("part-viii-",         "09-part-08-not-and-next.md"),
    ("part-ix-",           "10-part-09-authors.md"),
    ("colophon",           "11-colophon.md"),
]

SAMPLE_FILES = [
    "00-cover.md",
    "01-about.md",
    "02-part-01-manifesto.md",
    "03-part-02-how-cid-works.md",
]


def slug(chunk):
    for line in chunk.split("\n"):
        line = line.strip()
        if line.startswith("#"):
            title = line.lstrip("# ").strip()
            return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return ""


def assign_filename(index, chunk):
    if index == 0:
        return "00-cover.md"
    s = slug(chunk)
    # Prefix match, not substring match. "about" should match "about-this-document"
    # but must not also match "part-ix-about-the-authors".
    for marker, fname in FILENAME_MAP:
        if s.startswith(marker):
            return fname
    return f"unknown-{index:02d}.md"


def main():
    with open(SRC) as f:
        src = f.read()

    # Strip YAML frontmatter if present
    m = re.match(r"^---\n.*?\n---\n", src, re.DOTALL)
    if m:
        src = src[m.end():]

    # Split on \newpage directives
    chunks = [c.strip() for c in src.split("\\newpage") if c.strip()]

    os.makedirs(OUT, exist_ok=True)

    # Keep manuscript README in place
    preserved = {"README.md", "Book.txt", "Sample.txt"}

    # Remove old per-Part files
    for existing in os.listdir(OUT):
        if existing in preserved:
            continue
        if existing.endswith(".md"):
            os.remove(os.path.join(OUT, existing))

    files = []
    for i, chunk in enumerate(chunks):
        fname = assign_filename(i, chunk)
        with open(os.path.join(OUT, fname), "w") as f:
            f.write(chunk + "\n")
        files.append(fname)

    # Book.txt
    with open(os.path.join(OUT, "Book.txt"), "w") as f:
        for fname in files:
            f.write(fname + "\n")

    # Sample.txt
    with open(os.path.join(OUT, "Sample.txt"), "w") as f:
        for fname in SAMPLE_FILES:
            if fname in files:
                f.write(fname + "\n")
            else:
                print(f"warn: sample file {fname} not produced", file=sys.stderr)

    print(f"split {len(chunks)} Parts into {OUT}/")
    for fname in files:
        size = os.path.getsize(os.path.join(OUT, fname))
        print(f"  {fname:40s}  {size:>7} bytes")


if __name__ == "__main__":
    main()
