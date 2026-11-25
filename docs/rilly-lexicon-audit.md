# Rilly 2003 Vol. II lexicon audit

## Source, verified

- File: ~/workspace/meroitic-decipherment-datasets/downloads/rilly-2003-vol2-lexicon.pdf
- Size: 123,648,388 bytes, 304 pages
- Title: Le méroïtique. Données grammaticales, lexicales, position linguistique. Vol II. Lexique méroïtique
- Author: Claude Rilly, EPHE 2003, NNT 2003EPHE4068, HAL tel-04793700
- Text layer: none. pdftotext returns 1 byte on pages 10 and 50. Pages 1 to 3 are the HAL cover with text. Pages 4 to 304 are scanned images, 200 dpi JPEG, 1646 by 2331 px.
- Images extracted: 305 embedded JPEGs in raw/img/, one full page scan per PDF page, by pdfimages in 70 seconds.

## Volume structure, read from the page images

- PDF 1 to 3: HAL cover
- PDF 4 to 9: introduction, "Lexique méroïtique", about 800 entries, few with a real translation, often hypothetical
- PDF 10 to 13: glossary of language names cited in the volume, not lexicon entries
- PDF 14: blank page
- PDF 15 to 279: lexicon proper, alphabetical, entries start with the letter a
- PDF 280 to 304: "Gloses non retenues", rejected glosses, about 100 entries, headwords marked with an asterisk
- Entry pages to OCR: PDF 15 to 304, 290 pages. Front matter, PDF 1 to 14, holds no entries.

## Entry format, verified by reading the images

- Headword at the left margin, bold italic, sometimes with "(var. X)" variants, or an asterisk in the rejected section
- Body indented, starts with part of speech in italic, then discussion with REM citations, then a "Biblio. :" line
- Examples seen: -/a/ suffixe verbal, a- préfixe verbal, Abel toponyme REM 0551 and 0566, Adomn toponyme REM 1064/3 and 1094/7, Adonili toponyme REM 0094/30 and 32, ahide verbe, gloss "présenter", "offrir", "envoyer", REM 1003 and 1182
- Rejected examples: *ab substantif "bouche" selon Zyhlarz, *abe pronom, *ahide adjectif "profitable", *yindi adverbe "aujourd'hui", REM 0125

## OCR speed, measured on this cell

- Tesseract 5.3.4 LSTM, French, half-size page (823 by 1165): page 4, nearly blank, 19.1 seconds. Page 5, dense text: timed out after 900 seconds, 0 lines. Page 20, entry page: timed out after 280 seconds, 0 lines, 75.6 seconds of CPU used. Quarter-size page (411 by 582): timed out after 120 seconds, 0 lines.
- Tesseract legacy engine (--oem 0): not available, the installed fra.traineddata is LSTM only.
- Tesseract was wiped by a VM restart and had to be reinstalled by apt. It does not persist across restarts.
- RapidOCR, full resolution, warm: page 5, 278 seconds first run including model load. Page 10, 225 seconds. Page 15, 166.5 seconds. Page 20, no angle classifier: 133.2 seconds, 33 lines.
- Fastest measured route: RapidOCR without angle classifier, 133 seconds per page.
- No route finishes a page in under 60 seconds. Tesseract never finished an entry page at any size.
- Cell load during the tests: 1 minute average 17 to 33, from other agents' jobs. The cell has 1.5 shared CPUs. Parallel OCR across pages would split the same starved CPU, so it would not help.
- Time for all 290 entry pages at 133 seconds per page: about 10.7 hours of wall time, if run without interruption. At 167 to 225 seconds per page: 13.5 to 18 hours.

## Coverage now

- Pages with OCR text: 4 (tesseract, nearly blank), 5 and 10 (RapidOCR, front matter), 15 (RapidOCR, entry page)
- Entry pages with OCR text: 1 of 290
- Entries parsed: 3, all from PDF page 15
- Gold sample, hand read from the page images: 10 entries in gold-sample-v1.json, PDF pages 15, 20, 280, 304
- Parser check on page 15: 3 of 3 entries match the gold sample on form, part of speech, attestations and variants
- Parser fixes made after the check: letter-table words are skipped, single-letter headwords are skipped, low-confidence RapidOCR lines under 0.75 are dropped, REM citations without a space (REM0566) are caught, joined words (toponymedelocalisation) still yield the part of speech

## Overlap with the 774-entry lexicon

- Parsed entries: 3. Of these, 0 match a form_norm in lexicon.json. All 3 are new by form: -/a/, a-, Abel.
- This says nothing about the whole volume. It is 3 entries from the first page.
- The volume holds about 800 entries per its own introduction. A real overlap count needs the full OCR run.

## OCR quality problems, seen on pages 5, 10, 15

- Words joined with no space: "toponymedelocalisationinconnue", "Lapresentelisteestuneversioncorrigée"
- Diacritics dropped: é often becomes e, accents on capitals vanish
- The letter table signs become junk lines, for example "2s" at confidence 0.59
- French text reads well at confidence 0.93 to 1.00. Meroitic forms with dots below letters (ahide, Adonili variant Adenile) lose the dot in OCR, so form and form_norm strip it and the printed form is kept only in the gold sample
- No page was unreadable. No entry was guessed.

## What is blocked

- Full-book OCR on this cell. The fastest route needs about 11 hours of wall time for 290 pages, and the cell load is 17 to 33 from other work.
- What would unblock it: a machine with a free CPU, or a cloud OCR service, or Richardson running the OCR batch on his own Mac.
- The batch scripts are ready and resumable: tess_all.py (tesseract, not recommended, it never finished an entry page) and ocr_all.py (RapidOCR, 133 seconds per page without angle classifier, set use_angle_cls=False in ocr_all.py before a full run).

## Files in this folder

- rilly-2003-lexicon-v0.1.json: 3 entries from PDF page 15, partial, coverage stated in the file
- gold-sample-v1.json: 10 entries hand read from the page images, for parser validation
- parse_lexicon.py: parser, validated 3 of 3 on page 15 against gold
- ocr_all.py: RapidOCR batch script, resumable, skips pages already done
- tess_all.py: tesseract batch script, resumable, not recommended
- raw/img/: 305 extracted page JPEGs
- raw/page_005.ocr.txt, raw/page_010.ocr.txt, raw/page_015.ocr.txt: RapidOCR text
- raw/page_004.tess.txt: tesseract text, nearly blank page
- ocr_progress.log, tess_batch.log, tess_progress.log, parse_log.txt: run logs

---

# Mac OCR build, Nov 24, 2026: full volume done

- Built on Richardson's MacBook Pro via Tailscale SSH, after he authorized this machine's key.
- Mac: 12 CPUs, 24 GB RAM, macOS 27.0.1, arm64. Python 3.12.8, poppler 26.03.0, RapidOCR without angle classifier.
- pdfimages: 309 page images in 2.4 seconds.
- OCR: 290 pages in about 11 minutes, about 2 seconds per page, against 133 seconds per page on the sandbox cell.
- Parse: parse_lexicon.py, same parser, 744 entries, 818 KB.

## Counts

- Total entries: 744
- Lexicon proper (pages 15-279): 709
- Rejected glosses (pages 280-304): 35
- With a French gloss: 401
- With attestations: 539
- Gloss status: 707 proposed, 37 rejected

## Overlap with the existing 774-entry lexicon

- Old lexicon: 774 entries (107 certain, 664 proposed, 3 rejected).
- Overlap by normalized form: 85 entries.
- New by form: 655 entries.
- This grows the lexicon from 774 entries to about 1,429 distinct forms, before merging.

## Gold sample check, 10 of 10 parsed

- All 10 hand-read gold entries are in the parsed output.
- Diffs, all minor:
  - a-: attestations in a different order, same set.
  - Adomn: parsed REM 1064 only, gold also has REM 1094. The parser missed the second citation in "REM 1064/3, 1094/7".
  - Adonili: parser took "vers le Nord" from the discussion as a gloss, gold has no gloss.
  - aḥide: OCR read "presenter" for "présenter", accent lost.
  - abe: parser kept "pronom independant", gold says "pronom".
  - aḥide in the rejected section: pos and gloss empty, gold has "adjectif" and "profitable".
- No entry is invented. No gloss status is upgraded. All glosses stay "proposed" unless Rilly marks them otherwise.

## Zero-entry pages, 21 of 290, sampled

- Pages 52, 67, 113, 114 checked against their OCR text:
  - Page 52: continuation of a long discussion paragraph, no new headword. Correct.
  - Page 67: blank page, only the page number. Correct.
  - Page 113: blank page, only the page number. Correct.
  - Page 114: letter sign table only. Correct.
- The other 17 zero-entry pages were not individually read. Spot-check them before v1.0.

## Duplicate forms, 4, all genuine

- ahide: once in the lexicon ("présenter; offrir; envoyer"), once in the rejected section.
- dime: once in the lexicon, once in the rejected section ("contentement").
- hr: two lexicon entries, verb "manger; procurer; nourrir" and noun "Nord; le bas".
- mhe: two entries on page 125, one without gloss, one with "eau; pain; abondant". Check whether this is one split entry before v1.0.

## Limits

- OCR drops some accents (é read as e) and misses some citations after a comma.
- 21 zero-entry pages: 4 sampled and explained, 17 not yet read.
- The mhe double entry is unresolved.
- This is v0.1. Merge with the 774-entry lexicon and re-run the blind benchmark before calling it v1.0.
