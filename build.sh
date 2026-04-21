#!/usr/bin/env bash
#
# Builds dist/field-report-v0.pdf from FIELD_REPORT_V0.md.
# Requires: pandoc, xelatex.
#
# Usage:
#   ./build.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$ROOT/FIELD_REPORT_V0.md"
OUT_DIR="$ROOT/dist"
OUT="$OUT_DIR/field-report-v0.pdf"

mkdir -p "$OUT_DIR"

command -v pandoc >/dev/null || { echo "error: pandoc not found"; exit 1; }
command -v xelatex >/dev/null || { echo "error: xelatex not found"; exit 1; }

echo "building $OUT from $SRC..."

pandoc "$SRC" \
  -o "$OUT" \
  --pdf-engine=xelatex \
  --variable=geometry:letterpaper \
  --variable=geometry:margin=1in \
  --variable=fontsize:11pt \
  --variable=mainfont:"DejaVu Serif" \
  --variable=sansfont:"DejaVu Sans" \
  --variable=monofont:"DejaVu Sans Mono" \
  --variable=linestretch:1.25 \
  --variable=documentclass:article \
  --toc \
  --toc-depth=2 \
  --highlight-style=tango

echo "done: $OUT"
