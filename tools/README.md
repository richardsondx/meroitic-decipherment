# Tools

Custom tools built for this project. All are Python 3, standard library only unless noted. No tool calls a paid model. No tool needs network access, except where noted. Read each script before you run it.

## recompute.py

Recomputes the benchmark scores from the corpus JSON files. It is a Python port of `tokenizeNormalizedMeroitic` and `matchToken` from the original TypeScript engine. It computes the vocabulary gap, the per-narrative coverage, and the leakage checks.

Run:

```bash
python3 tools/recompute.py
```

It reads the corpus JSON files and writes `u1-gap-list.json`, `u1-summary.json`, and `u5-benchmark.json`. It never edits a source file. Verified end to end on 2026-11-20, exit 0. It reproduced the v3 benchmark narratives exactly, including every leakage field.

Source: `kits/meroitic-decipherment-workbench/recompute.py` in the 2026-11-20 Handover run.

## merge_lexicon.py

Merges a new lexicon into the old one. Rules, in order:

1. Never upgrade a gloss status. New entries are proposed or rejected only.
2. Never invent a gloss, a form, or a loan status.
3. Dedup key is `form_norm`, lowercased and stripped. Same form, different claim stays as two records, flagged in the report.
4. A certain old entry wins. Keep its gloss and status. Merge attestations (union). Note the new gloss and page in the notes when it differs.
5. A proposed old entry wins as the base record. Merge attestations.
6. A status conflict keeps the old record and adds the new entry as a second record.

It writes a merge report JSON with counts, conflicts, and duplicates. Run it from the folder that holds the two lexicon files, and read its header comment first.

Source: `merge-benchmark/merge_lexicon.py`, used for the Nov 24, 2026 merge of the Rilly 2003 OCR lexicon (744 entries) into the 774-entry lexicon.

## build-hallof.py

Builds a machine-readable corpus from Hallof page text files. Input is a folder of `page_XX.txt` files, one per PDF page of the Hallof Vol. 7 excerpt (or the full volume). Output is one JSON record per Hallof text, with normalization and tokenization ported exactly from the original parser. It reproduces the original corpus on all 90 overlapping records, 0 differences on 17 fields.

Source: `hallof-build/build-hallof.py`. See `docs/hallof-excerpt-audit.md` for the verification.

## parse_lexicon.py

Parses Rilly 2003 Vol. II lexicon entries from OCR text into JSON. Input is one OCR text file per PDF page (pages 15 to 304). The lexicon proper runs pages 15 to 279. The rejected glosses ("Gloses non retenues") run pages 280 to 304. Validated 3 of 3 entries on page 15 against a hand-read gold sample, and 10 of 10 gold entries parse in the full run.

Source: `rilly-lexicon-build/parse_lexicon.py`. See `docs/rilly-lexicon-audit.md` for the parser limits (accents lost in OCR, some citations after a comma missed).

## ocr_all.py

Batch OCR for scanned lexicon pages with RapidOCR. Input is the embedded JPEG page scans. Output is one OCR text file per page, with one line per OCR line: confidence, tab, text. It skips pages already done, so the run is resumable.

Run:

```bash
python3 tools/ocr_all.py [first_page] [last_page]
```

Defaults: pages 4 to 304. Pages 1 to 3 have a real text layer and are skipped. Needs `rapidocr-onnxruntime` installed. On a 12-core Mac, 290 pages took about 11 minutes. On a small shared cell, the same run takes about 11 hours. Use `use_angle_cls=False` for speed; the angle classifier is not needed for these scans.

Source: `rilly-lexicon-build/ocr_all.py`. The Mac kit in `tools/mac-ocr-kit/` wraps it for a Mac run.

## extract_attestations.py and build_retest_json.py

Contextual testing of a proposed gloss, the U3 method. `extract_attestations.py` pulls every occurrence of a candidate form from the corpus, with a window of surrounding tokens and the stored translation. The two REM 0094 witnesses are flagged so they count as one inscription. `build_retest_json.py` builds the verdict file from hand-judged verdicts. A candidate needs at least 3 decided inscriptions to count as supported. A meaning is supported only when it fits across multiple independent inscriptions. No gloss is upgraded.

Source: `merge-benchmark/u3-retest/`. See `docs/u3-retest.md` for the results: 1 supported, 0 refuted, 40 untested, 32 unjudged.

## mac-ocr-kit/

A ready-to-run kit for the full OCR batch on a Mac. It holds `run_mac.sh`, `ocr_all.py`, `parse_lexicon.py`, `gold-sample-v1.json`, `pipeline.md`, and `README_MAC.md`. Copy the kit to a Mac, put the scanned PDF in `~/Downloads`, and run `bash run_mac.sh`. It extracts the page images with poppler, runs RapidOCR without the angle classifier, and parses the lexicon. The Rilly 2003 batch finished 290 pages in about 11 minutes on a 12-core MacBook Pro.

Source: `rilly-lexicon-mac-kit/`, built Nov 24, 2026.
