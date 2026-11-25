# Griffith alternative corpus — audit

Date: 2026-11-20. Corpus file: `griffith-corpus-v0.1.json`.
Sources: Internet Archive djvu text of three public-domain volumes.
No purchase, no email, no publish. Nothing in this build edits a source file.

## Headline

- 238 records: Part I 42, Part II 50, Karanog 146.
- 15 records match a REM number. All 15 are inside the Hallof excerpt range 0001-0092.
- 223 records match no REM number. 146 of them are Karanog or Shablul texts.
- 158 records carry a translation. 2,457 translation words in total.
- 0 records carry a transcription. This is by design, not a gap in the parser.

## Premise correction

Griffith prints the Meroitic text in Meroitic cursive type, not in Latin transliteration.
The djvu OCR renders those glyphs as unreadable symbol strings, for example
Part I No. 1: `1-klP^[^A9]>f [U^Ws`.
There is no Latin transliteration of the full text anywhere in these volumes.
Latin script appears only as romanized names and words inside the discussion
and in the word indices at the back of each volume.
So `transcription_raw` and `transcription_norm` are empty on every record.
The OCR glyph lines are kept separately in `transcription_ocr_glyphs`,
flagged `ocr_unreliable`, and are never presented as text.
The earlier assumption that Griffith gives Latin transliterations was wrong.
What Griffith adds is the catalogue, English translations, names and parentage,
terminal formulae, and romanized words in discussion and indices.

## Counts per volume

Record words count title plus description plus translation words.
Meroitic tokens cannot be counted because no transliteration is extracted.

| Volume | Texts | Record words | Translation words | Pages (distinct) | With translation | REM matched | Glyph lines | Discussed words |
|---|---|---|---|---|---|---|---|---|
| Part I (1911) | 42 | 3,992 | 145 | 52-89 (22) | 12 | 10 | 18 | 9 |
| Part II (1912) | 50 | 5,809 | 543 | 10-58 (24) | 34 | 5 | 48 | 43 |
| Karanog (1911) | 146 | 15,206 | 1,769 | 55-77 (12) | 113 | 0 | 0 | 68 |
| Total | 238 | 25,007 | 2,457 | — | 158 | 15 | 66 | 120 |

Translation status: Part I none 30, partial 6, published 6.
Part II none 16, partial 19, published 15.
Karanog none 33, partial 113, published 0.
Karanog "partial" translations are commemorates and born-of sentences,
not full translations of the inscription.
121 Karanog records carry terminal formulae letters.
103 records carry museum numbers. 22 carry plate references.
3 records have page None: Part II 75, Kar. 1, Kar. 2.

## REM matching

Method: scoring, greedy, one REM per entry and one entry per REM.
Berlin museum number +6. Citation page equals entry page +3.
Citation page inside the entry page range +2. Site agrees +2.
A distinctive REM title word in the entry heading or description +2.
Accept only at score 5 or more with a margin of 2 over the next best pair.
Karanog records are never matched. Their page numbers belong to a different
book and would collide with Part I pages, and their REM numbers are not
determinable from the sources held.

Matched, 15:

| Griffith | REM | Score | Method | Confidence |
|---|---|---|---|---|
| Part I 1 | 0001 | 5 | page+site+title | likely |
| Part I 43 | 0044 | 7 | page+site+title | certain |
| Part I 45 | 0045 | 7 | page+site+title | certain |
| Part I 46 | 0046 | 7 | page+site+title | certain |
| Part I 49 | 0049 | 7 | page+site+title | certain |
| Part I 50 | 0050 | 7 | page+site+title | certain |
| Part I 59 | 0059 | 6 | berlin-number | likely |
| Part I 60 | 0060 | 6 | berlin-number | likely |
| Part I 65 | 0065 | 7 | page+site+title | certain |
| Part I 74 | 0074 | 5 | page+site+title | likely |
| Part II 75 | 0075 | 6 | berlin-number | likely |
| Part II 80 | 0080 | 6 | berlin-number | likely |
| Part II 84 | 0084 | 7 | page+site+title | certain |
| Part II 88 | 0088 | 5 | page+site+title | likely |
| Part II 89 | 0089 | 7 | page+site+title | certain |

No REM number is claimed twice. No Karanog record carries a REM number.
Berlin numbers were verified by hand for entries 41 (7261), 47 (2264),
48 (2263), 49 (2253), 50 (2266). Entries 41, 47, 48 stay unmatched:
41 is REM 0041 by Berlin number but its citation page does not agree,
so the matcher left it unmatched rather than guess.
That is a known conservative miss, not an error.
REM 0040 goes to entry 40, REM 0044 goes to entry 43 by the graffito keyword.
Entry 45 keeps REM 0045 by page and site.
61 REM records cite Griffith 1911 or 1912. 15 of 61 are matched here.
The rest cite pages whose entries are prose-discussed or missing from the OCR.

## Overlap with the 460-text corpus

- Overlap by rem_number: 15 records, all in the Hallof excerpt range 0001-0092.
  These are duplicates of Hallof excerpt texts, not new texts.
- Overlap by normalized transcription: 0.
  Every Griffith record has an empty transcription_norm, and the comparison
  was computed, not assumed.
- New texts not in rem-texts.json: 223 records.
  That is every record without a REM match.
  146 are Karanog or Shablul funerary monuments, a site with 0 texts in
  rem-texts.json. 77 are Part I or Part II entries whose REM number could
  not be fixed with certainty, including prose-discussed entries.
  "New" here means no REM number was assigned, not that the text is
  certainly absent from the REM catalogue under another number.

## What Griffith adds that the Hallof excerpt does not

- 146 Karanog and Shablul funerary monuments with names, parentage,
  titles, tomb numbers, Cairo museum numbers, and terminal formulae.
  0 Karanog or Shablul texts exist in rem-texts.json.
- English translations for 7 of the 62 Griffith-cited rem texts whose
  translation_status is none in rem-texts.json:
  REM 0046, 0049, 0065, 0080, 0084, 0088, 0089.
- 121 records with terminal formulae letters A to J, Karanog only.
- 103 records with museum numbers, 22 with plate references.
- 120 discussed romanized Meroitic words matched against the lexicon,
  with their source entry recorded.
- Site, object, and publication data for 238 inscriptions, all public domain.

## OCR quality

Glyph-heavy lines are lines with 3 or more characters from the set
`^ $ ~ * < | # \ { } [ ] _ = +`, counted in the body sections only.

- Part I body lines 5040-9574: 130 of 4,534 lines glyph-heavy, 2.9 percent.
- Part II body lines 897-7304: 332 of 6,407 lines glyph-heavy, 5.2 percent.
- Karanog catalogue lines 4394-6031: 31 of 1,637 lines glyph-heavy, 1.9 percent.

Worst pages, glyph-heavy lines out of total lines on that page:

- Part I: p. 64 (12 of 119), p. 79 (11 of 175), p. 89 (8 of 72),
  p. 83 (7 of 112), p. 73 (6 of 117), p. 81 (6 of 105).
- Part II: p. 9 (30 of 115), p. 18 (21 of 134), p. 10 (18 of 698),
  p. 40 (17 of 131), p. 60 (17 of 90), p. 39 (15 of 107).
- Karanog: page-level counting is unreliable because its page numbers live
  in running headers, not standalone lines. Body density 1.9 percent stands.

The glyph-heavy lines are the Meroitic text lines themselves, rendered as
symbols. English discussion lines are mostly clean. The worst pages are
worst because they hold the most Meroitic text, not because the English
is unreadable. No transliteration can be recovered from these lines.
The hand copies in Karanog pp. 127-181 are images, not OCR text, and were
not used.

## Missing numbers, with reasons

Part I, 32 missing of 1-74:
2, 3, 4, 5, 11, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32,
35, 36, 37, 38, 53, 54, 62, 63, 66, 67, 70, 73.
Most are discussed in prose without a standalone heading, especially
the Naga Lion temple gods 6-16 and their prose spans 17-38, and the
Meroe pyramid groups 62, 63, 66, 67, 70, 73.
REM 0023-0029 cite Griffith 1911 pp. 63-64, inside that prose span.

Part II, 19 missing of 75-121:
76, 79, 85, 86, 87, 91, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108,
109, 110, 111.
76, 79, 85, 87, 91 are prose-discussed or plate-only.
99-111 are the Philae graffiti discussed by Lepsius number, not by
Griffith entry number; their Lepsius numbers 7, 8, 9, 10, 13, 14, 15,
20, 21 appear as separate records in this corpus.
86 was a table row in the Philae graffiti comparison, not an entry,
and is excluded by design.

Karanog, 5 missing of 1-132: 11, 61, 110, 111, 114.
Shablul, 1 missing of 1-20: 11.
Headings for these are OCR-mangled or absent in the djvu text.

## Page limitations

- Part II 75 has page None. The Napata section starts on p. 7 per the
  contents list, and entry 75 is the first entry in it, so p. 7 is likely
  but was not verified from a page line, so it stays None.
- Part II 77, 78, 80, 81, 82, 83, 84 are recorded as page 10.
  That is the first page number the tracker caught. The contents list
  places the Napata section on p. 7 and the Soleb, Sedeinga, Sai, and
  Amara sections on p. 9. Their true pages are 7 to 9, not 10.
  The recorded value 10 is wrong for 77 to 83 and is kept only because
  the exact page per entry could not be pinned from the OCR.
- Kar. 1 and Kar. 2 have page None. The catalogue starts on p. 55 per the
  contents list, so p. 55 is likely but was not verified from a header line.
- Karanog page tracking uses running headers, which appear on alternate
  pages. Recorded Karanog pages are the last header seen, and can be
  one page early.

## Translation limitations

- Part II No. 94, the Kalabsha great inscription, has no continuous
  translation in Griffith. The record holds a fragment, "seed of the
  Sun-god", from piecemeal line readings.
- Part II No. 121 joins discussion quotes about the Lepsius graffiti.
  That is the entry discussion, not a translation of No. 121 itself.
- Karanog translations are commemorates and born-of sentences, partial
  by construction. The invocation "O Isis, O Osiris" is assumed at the
  start of each Karanog inscription and is not repeated in the record.
- Part I entries mostly have no translation, only discussion. 30 of 42
  Part I records have translation_status none.

## Spot check

10 records checked by hand against the source txt, 2026-11-20.
Heading, page, site, translation words, and REM number where assigned.
10 of 10 pass.

| Record | Heading in source | Page | Site | REM | Result |
|---|---|---|---|---|---|
| Part I 1 | 1. On base of kneeling ram | 52 | Soba | 0001 | pass |
| Part I 49 | 49. From Pyr. C 15 | 73 | Meroe | 0049 | pass |
| Part I 74 | 74. Stela of red granite | 89 | Dangel | 0074 | pass |
| Part II 75 | 75. Statue of black granite | None | Napata | 0075 | pass |
| Part II 94 | 94. The Meroitic inscription 5 | 27 | Kalabsha | none | pass |
| Part II 121 | 121. On the doorway | 45 | Philae | none | pass |
| Part II 137 | 137. Oblong altar | 58 | Philae | none | pass |
| Kar. 1 | Kar. I. Altar of fine pink sandstone | None | Karanog | none | pass |
| Kar. 45 | Kar. 45. Three fragments | 61 | Karanog | none | pass |
| Sh. 1 | Sh. I. Rectangular altar | 75 | Shablul | none | pass |

## Gaps and next steps

- The word indices are not yet extracted: Part II Index A lines 7526-9144,
  Karanog Index C lines 8264-10211, Part I index lines 9574-9867.
  They hold the only Latin-script Meroitic vocabulary in these volumes.
  A wordlist file is the clear next build.
- The 32 missing Part I and 19 missing Part II numbers need hand recovery
  from the prose spans and the plate captions. REM 0023-0038 sit in the
  Naga prose span, pp. 63-64.
- No text the lexicon never cites was found here. All 15 matched REM
  numbers are cited by the lexicon. A true blind test text is still missing.
- Entry 41, REM 0041 by Berlin number 7261, stays unmatched because its
  citation page does not agree. Hand review could confirm it.
- Reading status is griffith-1911 on every record. These readings are
  1911-1912 and are sometimes superseded by Hallof and Rilly.
  Do not treat a Griffith translation as current scholarship.
