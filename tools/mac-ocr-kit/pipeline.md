# Pipeline note: Rilly 2003 Vol. II lexicon

## Commands, in order

- Verify the PDF: pdfinfo ~/workspace/meroitic-decipherment-datasets/downloads/rilly-2003-vol2-lexicon.pdf
- Check for a text layer: pdftotext -f 10 -l 10 [pdf] - | wc -c (returns 1, no text layer)
- Extract page images: pdfimages -j -p [pdf] raw/img/page (305 JPEGs, about 70 seconds)
- OCR one page, RapidOCR, fastest measured route: python3 ocr_all.py 15 15 (uses RapidOCR, skips pages already done)
- OCR the full entry range, RapidOCR: python3 ocr_all.py 15 304 (about 11 hours at 133 seconds per page, resumable)
- Before a full run, set use_angle_cls=False in ocr_all.py: RapidOCR(use_angle_cls=False) cuts a page from about 167 seconds to about 133 seconds
- Parse OCR text into JSON: python3 parse_lexicon.py (writes rilly-2003-lexicon-v0.1.json and parse_log.txt)
- Spot check: compare parsed entries on a page against gold-sample-v1.json (see below)

## Tesseract route, not recommended

- Install: apt-get install -y tesseract-ocr tesseract-ocr-fra (does not survive a VM restart, reinstall after one)
- Batch: python3 tess_all.py 4 304
- Measured: tesseract never finished an entry page at half size (timed out at 280 seconds), quarter size (timed out at 120 seconds), or full size. Do not use it for this book on this cell.

## Spot check status

- A 20-entry spot check needs 20 parsed entries. Only 3 entries are parsed so far, all from PDF page 15.
- Check done: all 3 parsed entries match the gold sample on form, part of speech, attestations and variants.
- Gold sample: 10 entries hand read from the page images (PDF pages 15, 20, 280, 304) in gold-sample-v1.json.
- Run the 20-entry check after the OCR batch reaches about 10 entry pages, then compare parse output against fresh visual reads of those pages.
