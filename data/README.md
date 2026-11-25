# Data

This folder holds only data that is clearly licensed for redistribution. Every file lists its source and license below. Nothing here is pending-permission material. The full corpus and the merged lexicon are not in this folder. See the exclusions at the bottom for why, and how to obtain them.

## Included files

- `asjp-nes-comparative.json`: ASJP comparative forms for Northern East Sudanic languages (Nubian, Nara, Taman, Nyimang), 200 concepts, 897 forms. Source: Lexibank ASJP CLDF, https://github.com/lexibank/asjp. License: CC BY 4.0.
- `wiktionary-nes-rilly2010.json`: Raw Wiktionary API response for "Appendix:Northern Eastern Sudanic reconstructions", the reconstructed proto-forms from Rilly 2010, pages 420 to 529. These are reconstructions, never attestations. Source: https://en.wiktionary.org/wiki/Appendix:List_of_Northern_Eastern_Sudanic_reconstructions. License: CC BY-SA.
- `griffith-corpus-v0.1.json`: 238 records from Griffith 1911-1912 (Parts I and II, and Karanog). Our own build from the public-domain Internet Archive djvu texts. 0 transcriptions: Griffith printed Meroitic cursive type, not Latin transliteration, so the OCR glyph lines are kept separately and flagged unreliable. 158 records carry an English translation. Source texts: https://archive.org/download/archaeologicals20egyp/archaeologicals20egyp_djvu.txt. License: public domain.
- `rem-0413.json`: REM 0413, one text, 8 tokens, 4 lines, 3rd century CE, Temple of Amun M.260, Petrie Museum UC 44568. Our own structured record, following the corpus schema, from Elfiky 2025 (SHEDET Vol. 14, Issue 14, DOI 10.21608/shedet.2024.293858.1255), using the Hallof 2024 Vol. 7, page 58 reading. License: academic-fair-use-excerpt. A text the lexicon never cites, so a blind-test candidate.
- `rem-1141-sample.txt`: REM 1141, the Amanishakheto stele, 38 lines, 152 tokens. Joined transliteration from the Qasr Ibrim Vol. III publisher sample. Already published by Edwards and Rilly 2007. License: academic-fair-use-excerpt.
- `rem-1158-sample.txt`: REM 1158, a wooden plaque, 10 lines, 12 tokens. Joined transliteration from the same sample. Already published in REM 2000. License: academic-fair-use-excerpt.

## Excluded files, and why

- `rem-texts.json` (460 texts, 5,791 tokens): excluded. It holds the Hallof Vol. 7 excerpt (90 texts, pending-permission) and Otten corpus material (no license file). See `docs/corpus-manifest.json` for the counts and sources, and `docs/rem-acquisition-plan.md` for how to obtain each part.
- `lexicon.json` (774 entries) and `lexicon-merged-v0.2.json` (1,432 records): excluded. They mix Rilly gold entries (academic-fair-use-excerpt), Rilly 2003 OCR entries (HAL license not stated), and Otten-derived entries (no license). Counts, merge rules, and conflicts are in `docs/merge-report.json` and `docs/benchmark-merged.md`. The Rilly 2003 OCR lexicon can be rebuilt with `tools/ocr_all.py` and `tools/parse_lexicon.py` from the HAL PDF at https://hal.science/tel-04793700v1.
- `rilly-2003-lexicon-v0.1.json` (744 OCR entries): excluded. The HAL record carries the HAL distribution authorization, not an open redistribution license. The audit summary is in `docs/rilly-lexicon-audit.md`, with acquisition instructions.
- `hallof-excerpt-corpus-v0.2.json` (92 records, REM 0001 to 0092): excluded. The excerpt is a free publisher sample, but the book is under copyright (J.H. Roll, 2024). Permission status is pending-permission. The audit is in `docs/hallof-excerpt-audit.md`. The excerpt PDF is free at https://www.newbooks-services.de/MediaFiles/Texts/5/9783897546295_Excerpt_002.pdf.
- Otten corpus files (`mero-corpus.txt`, `MilletExamples.txt`, `RillyExamples.txt`, `LobbanVocabList.txt`, royal narratives, bilingual dicts, embeddings): excluded. The GitHub repo has no LICENSE file, so public visibility is not a license. Get them from https://github.com/Joshua-Otten/Meroitic-Corpus and confirm reuse with the authors.

## Rule

Never present pending-permission data as open. If a file is not listed above as included, it is not in this folder for a reason. If you can clarify a license, open an issue with the source link.
