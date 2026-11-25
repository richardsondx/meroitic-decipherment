#!/bin/bash
# Run the Rilly lexicon OCR batch on a Mac.
# Usage: bash run_mac.sh [first_page] [last_page]
# Defaults: pages 15 to 304 (lexicon proper 15-279, rejected glosses 280-304).
# Resumable: pages already OCR'd are skipped.
set -e
cd "$(dirname "$0")"
FIRST=${1:-15}
LAST=${2:-304}
PDF="rilly-2003-vol2-lexicon.pdf"
if [ ! -f "$PDF" ]; then
  if [ -f ~/Downloads/"These Rilly EPHE 2003 Vol 2 Lexique meroitique.pdf" ]; then
    echo "Copying PDF from Downloads..."
    cp ~/Downloads/"These Rilly EPHE 2003 Vol 2 Lexique meroitique.pdf" "$PDF"
  else
    echo "PDF not found. Put 'These Rilly EPHE 2003 Vol 2 Lexique meroitique.pdf' in this folder or in ~/Downloads, then run again."
    exit 1
  fi
fi
command -v pdfimages >/dev/null 2>&1 || { echo "pdfimages not found. Run: brew install poppler"; exit 1; }
python3 -c "import rapidocr_onnxruntime" 2>/dev/null || { echo "rapidocr-onnxruntime not found. Run: python3 -m pip install rapidocr-onnxruntime"; exit 1; }
mkdir -p raw/img
if [ -z "$(ls raw/img/page-*.jpg 2>/dev/null)" ]; then
  echo "Extracting page images from the PDF (about 70 seconds)..."
  pdfimages -j -p "$PDF" raw/img/page
else
  echo "Page images already present, skipping extraction."
fi
echo "Starting OCR, pages $FIRST to $LAST. This takes about 133 seconds per page. Stop with Ctrl-C any time, it resumes where it left off."
python3 ocr_all.py "$FIRST" "$LAST"
echo "OCR done. Now parse with: python3 parse_lexicon.py"
