# Hallof Vol. 7 excerpt audit

- Corpus file: `hallof-excerpt-corpus-v0.2.json`
- Pipeline: `build-hallof.py`
- Source: publisher excerpt PDF, 23 pages, 3,286,514 bytes, in
  `source-meroe-philology/data/raw/hallof/hallof-2024-excerpt.pdf`
- Page text files: `page_01.txt` to `page_23.txt` in the same folder
- Date checked: 2026-11-20

## Counts, recomputed

- Records: 92
- REM range: 0001 to 0092
- Total tokens: 1254
- Complete records: 89
- Zero-token record: 1 (REM 0012)
- Non-Meroitic record: 1 (REM 0072)
- Truncated record: 1 (REM 0092)
- Inscription pages: 15 (PDF pages 9 to 23, inscription pages 1 to 15)
- Front matter pages: 8 (PDF pages 1 to 8)
- Blank pages: 2 (PDF pages 6 and 8, blank in the PDF itself, confirmed by pdftotext)
- Texts per inscription page: 6.1 (92 divided by 15)
- Tokens per inscription page: 83.6 (1254 divided by 15)
- Mean tokens per transcribed record: 13.9 (1254 divided by 90)
- Script: 50 hieroglyphic, 42 cursive
- Language: 74 Meroitic, 18 Meroitic plus Egyptian
- Genre: 73 temple or royal inscription, 14 funerary or votive, 3 rock inscription or graffito, 1 royal dedication, 1 royal bark stand
- Records with no certainty words: 19
- Records using a fallback publication line: 0

## The 0001-0091 vs 0001-0092 discrepancy, resolved

- The manifest in `corpus-manifest.json` says the excerpt holds REM 0001 to 0092.
- The data in `rem-texts.json` holds 90 Hallof texts, REM 0001 to 0091.
- Both are right about different things. The range is 0001 to 0092. The count is 90 in `rem-texts.json` and 92 in this corpus.
- Reason 1: REM 0072 is in the excerpt, on PDF page 20, but its note says "obviously a non-Meroitic inscription" and it has no transcription lines. The original parser skipped entries with no transcription lines, so REM 0072 never entered `rem-texts.json`.
- Reason 2: REM 0092 is in the excerpt, on PDF page 23, with object, findspot, present location, dating, publication, and note, but no transcription lines. The free excerpt ends in the middle of the REM 0092 entry, after its note and before its first transcription line. The original parser skipped it for the same reason.
- Evidence: page 23 tail, read in full, ends with the REM 0092 note "compared with the original Philae photo" and no numbered lines. Page 20, read in full, shows REM 0072 with a note and no numbered lines.
- Resolution: this corpus holds 92 records. REM 0072 is kept with status `non-meroitic`, token count 0. REM 0092 is kept with status `truncated`, token count 0. Neither invents a transcription.
- The earlier queued gap "check why REM 0012 holds 0 tokens" is also resolved here. REM 0012 holds one transcription line, `(1) ---·`, which is only lost signs. Its token count is 0 because the tokenizer drops `---` runs. That is correct, not a bug.

## Texts in the excerpt that are NOT in rem-texts.json

- REM 0072, PDF page 20, inscription page 12, status non-meroitic, 0 tokens. Reason: Hallof marks it non-Meroitic, no transcription exists to ingest.
- REM 0092, PDF page 23, inscription page 15, status truncated, 0 tokens. Reason: the free excerpt ends mid-entry, the transcription is on the next page, which is not in the free excerpt.
- No other excerpt text is missing from `rem-texts.json`. The other 90 records match it exactly, see below.

## Verification against rem-texts.json

- Compared all 90 overlapping records field by field, on 17 fields: transcription_raw, transcription_norm, token_count, lines, title, site, findspot, present_location, support, script, date, language, genre, is_formulaic, publication, certainty_words, notes.
- Differences: 0. Every field matches on every record.
- Token total matches: 1254 in both files.
- This means the Python pipeline reproduces the original TypeScript parser exactly on this excerpt, including its group-metadata inheritance and its normalization.

## Spot checks by hand, 10 records

- For each record below, every line of its transcription_raw was checked against its page text file. All lines were present.
- REM 0001, PDF page 9, complete, 12 tokens, 8 lines checked, all present.
- REM 0009, PDF page 10, complete, 1 token, 2 lines checked, all present.
- REM 0012, PDF page 10, zero-token, 0 tokens, 2 lines checked, all present.
- REM 0021, PDF page 11, complete, 8 tokens, 15 lines checked, all present.
- REM 0041, PDF page 15, complete, 20 tokens, 10 lines checked, all present.
- REM 0059, PDF page 18, complete, 23 tokens, 24 lines checked, all present.
- REM 0072, PDF page 20, non-meroitic, 0 tokens, no transcription lines to check.
- REM 0084, PDF page 22, complete, 60 tokens, 14 lines checked, all present.
- REM 0091, PDF page 23, complete, 24 tokens, 22 lines checked, all present.
- REM 0092, PDF page 23, truncated, 0 tokens, no transcription lines to check.
- Result: 10 of 10 spot checks pass.

## Page text provenance

- The page text files were extracted with pdfjs by the original builder, not with pdftotext.
- A fresh pdftotext run on the same PDF gives the same words in a different case and line layout on 19 of 23 pages. Example: pdfjs gives "reM", "note:", "rock inscription", while pdftotext gives "RE", "Note:", "Rock inscription", with tab characters.
- Content is the same. Case and line breaks differ. That is why a raw string comparison between the two extractions fails, while the token-level spot checks pass.
- The delivered corpus is built from the page text files, and it matches `rem-texts.json` on all 90 overlapping records. That match is the stronger check, because `rem-texts.json` was built from the same pdfjs extraction.

## Gaps and unreadable pages

- PDF pages 6 and 8 are blank in the PDF itself. They are not missing text. Page 6 follows the contents page. Page 8 follows the preface.
- No inscription page is unreadable. All 15 inscription pages have a full text layer.
- REM 0092 is the only entry cut off by the end of the free excerpt.
- REM 0073 sub-entry C is noted in Hallof as "obviously a non-Meroitic inscription". Its text is kept inside the REM 0073 record as printed, with the note preserved. It is not split out as a separate record, because Hallof gives it no REM number of its own.
- Group headers in the excerpt: REM 0003 to REM 0004, REM 0011 to REM 0016, REM 0017 to REM 0020, REM 0066 to REM 0067, and others. Group metadata was inherited into child records exactly as the original parser did. No group header is itself a record.
- Uncertain readings are kept as printed. The characters `.`, `[ ]`, `( )`, and `---` are preserved in `transcription_raw` and in `transcription_norm`. No reading was upgraded from uncertain to certain.
- Permission status on every record is `pending-permission`. The excerpt is a free publisher sample, but the book is under copyright. No record here is a claim of open access.
