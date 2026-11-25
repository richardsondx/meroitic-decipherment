# Audit: Qasr Ibrim Vol. III sample (SRaT 9.5)

## Source

- Jochen Hallof, "The Meroitic Inscriptions from Qasr Ibrim, III. Inscriptions on Stone, Wood, Parchment and Gourd, Text", SRaT Vol. 9.5, J.H. Röll, 2020.
- ISBN 978-3-89754-576-2.
- File: 1576-SRaT-9-5-Leseprobe.pdf, a 21-page publisher sample (Leseprobe).
- PDF has a text layer. Extraction used pdftotext. No OCR was needed.
- The sample covers: cover, title, contents, preface (p. 7), introduction (pp. 9-10), and the start of the catalogue (pp. 11-21). The full book's catalogue runs pp. 11-206.

## Verdict in one line

- Yes. The sample prints 2 full transliterations outside our corpus range, REM 1141 and REM 1158. Both are re-publications of already published texts. No unpublished text is printed in the sample.

## Full transliterations printed in the sample

### REM 1141 [QI 1964/1]

- Object: sandstone stele, broken in two, top missing. 77 x 116 x 16 cm.
- Findspot: church, north aisle, reused in church flooring, Qasr Ibrim.
- Present location: British Museum, EA 1836.
- Content: royal inscription of Queen Amanishakheto and Prince Akinidad. Opens with aleqese, a written announcement. Lists donations of water, meat, asero, apnete, and mse.
- Lines: 38, of which the last 6 or more are lost. Line 38 is almost entirely destroyed.
- Tokens: 152. Method below.
- Status: already published. Edwards and Rilly 2007 (transliteration, photo, facsimile). This volume re-publishes it with a new drawing and improved readings.
- In our corpus: no. Checked against rem-texts.json. Not present.
- Joined transliteration saved as rem-1141-sample.txt.

### REM 1158 [QI 1976.02.07/4]

- Object: wooden plaque, 9.3 x 4.3 cm.
- Findspot: House X-30, refuse fill, Qasr Ibrim.
- Present location: Egyptian Museum Cairo, JdE 94226.
- Content: 5 lines recto, 5 lines verso, black ink, no word dividers. Untranslated in the sample. The commentary breaks off mid-sentence at the end of the sample.
- Lines: 10. Tokens: 12. Method below.
- Status: already published. REM 2000, 1704-1705; Hainsworth-Leclant 1983 (transliteration of the recto).
- In our corpus: no. Checked against rem-texts.json. Not present.
- Joined transliteration saved as rem-1158-sample.txt.

## Token count method for the sample texts

- The sample prints transliterations with spaced letters (a l e q e se). Each line was joined into words, then the corpus tokenizer (tokenize_normalized from build-hallof.py) was run.
- Calibration: the same tokenizer recomputes the stored token counts exactly on all four royal narratives (663, 481, 230, 693), so the method matches the corpus.
- A dot marks a lost sign inside a word, so dot-joined fragments count as one token (for example qesen.l is one damaged word, not two).
- Pure numerals are dropped, per the corpus rule. REM 1141 prints 1000, 100, and 20; all three are dropped. The token "+30" is kept by the stock tokenizer and counts as one token.
- Line 38 of REM 1141 is almost entirely lost. Its three legible fragments ([ne/d], [y], t[w]) count as three tokens, not one. Without this fix the count would be 150. With it, 152.
- REM 1158 verso line 3, "qerlidek . . [mq]", counts as one word. If it is two words, the count is 13, not 12.
- REM 1158 verso line 2 prints "t 10 d e". The 10 is dropped and the line counts as two tokens, terekest and de.

## REM numbers only cited or discussed, not printed

- 60 distinct REM numbers match the text. Four are false hits, not REM numbers: 1975, 1983, 1984 (years of preliminary REM publications) and 2000 (the year of the REM catalogue, cited as "REM 2000: 1670-1671").
- 56 real REM numbers are named. Minus the 2 printed in full, 54 are cited only.
- Seven more numbers come from ranges named in the introduction and never printed individually: 1172, 1178, 1179, 1199, 1325, 1326, 2069.
- The range REM 2692-2780 adds 85 more numbers never named individually (2692, 2705, 2732, and 2741 are named).
- Total cited-only distinct REM numbers: 146.
- Individually cited (54): 0017, 0020, 0049, 0075, 0078, 0085, 0086, 0089, 0094, 0359, 0405, 0406, 0427, 1001, 1003, 1041, 1044, 1067, 1138, 1160, 1162, 1163, 1171, 1177, 1182, 1198, 1228, 1232, 1248, 1251, 1273, 1293, 1294, 1322, 1324, 1361, 1367, 2030, 2044, 2050, 2068, 2071, 2112, 2136, 2186, 2201, 2209, 2210, 2293, 2445, 2692, 2705, 2732, 2741.
- Of these, 8 sit inside our Hallof excerpt range REM 0001-0092 (0017, 0020, 0049, 0075, 0078, 0085, 0086, 0089). They are cited as parallels, not printed.
- Most citations are parallels in commentary, not texts the volume publishes. For example REM 1044 is cited 10 times and REM 0094 7 times, only as parallels for words and phrases.

## What the full volume would add

- The preface says the catalogue holds 107 texts, of which only 17 were already published.
- The introduction says the main part is 88 hitherto completely unknown documents, REM 2692-2780, on stone, wood, parchment, and gourd.
- The re-published catalogue texts are 15: REM 1141, 1158, 1163, 1171-1172, 1177-1179, 1198-1199, 1228, 1248, 1324-1326.
- The appendix improves readings of 9 published texts (ostraka REM 1162, 2050, 2068-2069, 2071, 2136; papyri REM 1232, 2186, 2210), transliterates the papyrus fragments REM 2201, and adds the omitted drawing of REM 2293.
- None of the 15 re-published texts and none of the 11 appendix texts is in our corpus. Checked against rem-texts.json.
- So the full volume would add up to 107 catalogue texts to the corpus, of which 88 are completely new, plus improved readings for 11 more.
- Two numbers do not add up, and the sample does not resolve them. First, 17 published plus 88 unpublished is 105, not 107. Second, the range REM 2692-2780 spans 89 numbers, not 88. Both gaps are 1 to 2 texts. Do not treat 107 or 88 as exact until the full volume is checked.
- The preface also notes the volume's special value: many parallel texts and phrases, 39 examples of the so-called "décrets oraculaires amulétiques", and a summary chapter on grammar and word formation. That is the material the project needs for morphology and syntax, not just more words.

## What the sample does not give

- No transliteration of any of the 88 unpublished texts. The sample stops at REM 1158, before the unpublished section begins.
- No word index or summary pages. The sample ends at catalogue page 21 of 206.
- No plate volume (SRaT 9.6). Photos and drawings are cited by plate number only.
- REM 1141 and REM 1158 are useful, but they are re-publications. They add 164 tokens to the corpus, not new texts the field has never seen.

## Files written

- rem-1141-sample.txt: joined transliteration of REM 1141, 38 lines.
- rem-1158-sample.txt: joined transliteration of REM 1158, 10 lines.
- This audit.
