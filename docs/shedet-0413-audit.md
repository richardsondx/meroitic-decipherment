# Audit: REM 0413 from the SHEDET article

## Source

- Hend Elfiky, "A Voice from the Past: Analysing a Meroitic Cursive Inscription from the Temple of Amun M.260", SHEDET Vol. 14, Issue 14 (2025), pp. 404-422.
- DOI: 10.21608/shedet.2024.293858.1255.
- Author: Faculty of African Postgraduate Studies, Cairo University.
- Received 30 May 2024. Accepted 5 Sep. 2024. Online 19 Feb. 2025.
- PDF has a text layer. Extraction used pdftotext. No OCR was needed.

## What was extracted

- One text: REM 0413, 4 lines, 8 tokens.
- Tokens: wbrxmlo, ye, sorli, yinsidekeli, nkeyi, mkedokeli, yinsidekeli, nmlro.
- Token count method: the corpus tokenizer (tokenize_normalized from build-hallof.py, the exact port of tokenizeNormalizedMeroitic). It splits on whitespace and word dividers and drops pure numerals. Recomputed token counts match the stored counts exactly on all four royal narratives, so the method is the same as the corpus.
- Transcription_raw follows Hallof 2024 Vol. 7, 58 as printed in the article (pp. 407-408).
- Normalization follows the corpus schema: ḫ becomes x, the word divider becomes " : ".
- Translation is the article's tentative translation, kept as proposed, not certain.
- Record file: rem-0413.json, in the same 33-field shape as rem-texts.json.
- source_tag: elfiky-2025-shedet-rem0413. permission_status: academic-fair-use-excerpt.
- Split is shedet-0413, a new split, so the record stays out of every existing evaluation split.

## Content in one line

- A pilgrim's short prayer on a temple block: a man named Wbrxmlo invokes Osiris and Makedoke, with a second name Nkeyi, and ends on the unknown word nmlro.

## Metadata

- Findspot: Temple of Amun M.260, steps of Room M.275, Meroe.
- Excavator: John Garstang, 1909-1910 season (Garstang et al. 1911, 70-71, pl. LXVIII, 13).
- Left fragment, with the inscription: Petrie Museum, London, UC 44568 (also LDUCE-UC44568, P.DC-WEC9/S4), 39.0 x 30.4 x 7.3 cm.
- Right fragment, graffito only, no text: Egypt Centre, Swansea, EC 1304, 21.9 x 29.5 x 7.5 cm.
- Neither fragment is on display. Both are in store.
- Script: cursive. Reading direction: right to left.
- Date: 3rd century CE (Meroitic Tardif), following Rilly and Hallof (Hallof 2024 Vol. 7, 58).
- Genre: pilgrim invocation. The article links it to invocation formula style f, which is rare (Zach 2017, 267).

## Three readings, and which one was used

- Griffith (1911) reads the signs in left-to-right order: ilro sey:olmhrbw / iyekn:ilekedisniy / ileked isniy:ilekodekm / oremn. This is the mirror order of the same text, because the inscription reads right to left.
- Heyler (1966-1967, 132 n.91) reads: w-br h-mle-y sere-i yi-nsi-deke-li: nke-yi Mke-deke-li: yi-nsi-deke-li: nhe-re.
- Hallof (2024 Vol. 7, 58) reads: wbrḫmlo: ye. sorli. / yinsidekeli: nkeyi. / mkedokeli: yinsidekeli. / nmlro.
- The record uses Hallof, the most recent reading and the one the corpus treats as authoritative. Griffith and Heyler are kept in the notes field.

## Uncertainties

- The -ye ending: Hallof notes the scribe cut the word divider in the wrong place and added the final e later, higher up. So -ye is a personal-name suffix, not a separate word. The record keeps it as a token because the corpus tokenizes on dividers, but the note flags it.
- Nmlro: unknown from other texts. Hallof calls it the last word of an invocation of Makedoke. The article treats it as a verbal form. No gloss is given.
- The word divider after wbrḫmlo is partly melted into the first stroke of y. The reading is Hallof's, not independently checked against a photo.
- The graffito on the same block may date to the mid-1st century BCE, older than the inscription. The two are not dated together.
- The sign transcribed as x (3rd h) in wbrxmlo and the sign transcribed as x in nkeyi follow Hallof. No independent check was made.
- Translation status is proposed. The article calls it a tentative translation. It is not a published word-level translation in the strong sense.

## Certainty words: one honest warning

- certainty_words is ["ye"], by the same form-match method the Hallof build used.
- But the lexicon's certain glosses for ye are "south / southern region" and "optative / 3rd-person verbal prefix". Neither is the personal-name suffix use in this text. The match is by form only, not by sense.
- Sorli (Osiris with article and vocative) is NOT in certainty_words. The lexicon holds "soreyi" as certain (Osiris), but the bare form "sor" is only proposed (glossed "livre; scribe"). So the theonym does not count as certain under the corpus method.
- Five of the eight tokens are forms absent from the merged lexicon entirely: wbrxmlo, sorli, yinsidekeli, nkeyi, mkedokeli, nmlro (yinsidekeli occurs twice, so 7 of 8 tokens sit in forms the merged lexicon never lists). Only ye is present.
- That makes REM 0413 a text the lexicon never cites. It is a candidate for a true blind test, which the project still lacks.

## What was not done

- rem-texts.json, lexicon.json, and every merged file were not touched. Merging needs a separate approval.
- No new lexicon entries were made from this text. Its new forms are listed here only.
