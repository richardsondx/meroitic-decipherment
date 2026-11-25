# Minimum viable corpus for Meroitic decipherment

## What "viable" means here

A corpus that lets a system learn and be tested on Meroitic without pretending to be a full decipherment. It must contain: real Meroitic text in transcription, the words we are sure about, a way to score a prediction, and a small set of known-language material to align against. It must not be inflated by synthetic data presented as real text.

## The files (all in `downloads/` unless noted)

### Tier 1 — the machine-readable core (use first)
- `otten-meroitic-corpus/mero-corpus.txt` — 18,090 lines, 756,028 tokens. This is the ONLY machine-readable Meroitic corpus. Warning: it is mostly synthetic (871 real example texts/phrases name-swapped to 17,257 sentences). Treat the 871-source count as the real size; treat augmented lines as training data only, never as evidence of a text.
- `otten-meroitic-corpus/MilletExamples.txt` — 1,447 lines of real example phrases (Millet 1968).
- `otten-meroitic-corpus/RillyExamples.txt` — 40 lines of Rilly 2007 example phrases.
- `otten-meroitic-corpus/LobbanVocabList.txt` — 200-line vocabulary list (source bibliographic record not verified; flag it).
- `otten-meroitic-corpus/TanyidamaniNarrative.txt` — REM 1044, the longest text (161 lines), with translation.
- `otten-meroitic-corpus/HamadabStelaOfAmanirenasNarrative.txt` — REM 1003.
- `otten-meroitic-corpus/KalabshaMeroiticInscriptionOfKharamadoyeNarrative.txt` — REM 0094 (Kharamadoye).
- `otten-meroitic-corpus/bilingual_dicts/` — seven Meroitic-Egyptian alignment dictionaries (91+ pairs: nouns 26, names 18, numbers 15, verbs 14, titularies 9, adjectives/adverbs 6, prepositions 3).
- `otten-meroitic-corpus/embeddings/` — Meroitic and Egyptian Word2Vec embeddings, dims 20/50/100/120.
- `otten-2025-alp-1.11.pdf` — the paper; Table 1 is the count sheet (193 translated words, 897 phrases, 302 Late-Egyptian texts, 708 scanned Nubian pages).

### Tier 2 — the sure vocabulary (the gold set)
- Rilly 2003, Vol. II lexicon (~800 entries, graded, with a quarantined "Gloses non retenues" addendum) — the authoritative lexicon. PDF is 123,648,388 bytes on HAL; download it from a fast connection (see inventory Rank 2). Only ~100 words are translatable "with some certainty" (Rilly 2016); the rest is proposed, graded.
- Hallof 2024, Vol. 7 Documents — transliterations REM 0001-2780. Print only; the excerpt PDF is in `downloads/hallof-2024-excerpt.pdf`. Buying or requesting this volume is the single biggest real-text gain.
- Rilly 2016 UEE "Meroitic" (`downloads/rilly-uee-2016-meroitic.pdf`) — the authoritative count sheet and genre breakdown (half the published corpus funerary; ~250 graffiti; 16 amuletic; ~70 ostraca).

### Tier 3 — comparative evidence (for the cognate channel)
- `downloads/gld-nubian-swadesh-starostin.pdf` — Starostin Nubian 100-item lists (11 lects), 67 pp.
- ASJP CLDF (GitHub lexibank/asjp) — Nara, Dongolese/Kunuz Nubian, Afitti, Ama, Sungor, Tama, Nobiin 40-item lists.
- DBMNT (https://dbmnt.pcma.uw.edu.pl/) — Old Nubian metadata/names (4,518 texts), CC BY 4.0, exportable XML/CSV/Excel; no full-text corpus.
- Rilly 2010 (print) — the 43-word comparison + ~170 reconstructed Proto-Northern East Sudanic forms. Reconstructions are hypotheses, never attestations.

### Tier 4 — parallel / known-language text
- `downloads/fhn-vol1-djvu.txt` — FHN Vol. I full text (OCR). Egyptian, Demotic, Greek, Latin and Coptic sources with English translations; Meroitic entries have transliteration but no consecutive translation.
- `downloads/griffith-1912-meroitic-inscriptions-II-djvu.txt` — Griffith's primary transliterations (public domain, OCR rough).
- Gallus trilingual (OGIS 654, https://www.attalus.org/docs/ogis/s654.html) — Egyptian/Latin/Greek; names a Meroitic king; not a Meroitic translation.
- Wad Ben Naga bark stand REM 0041 (Berlin ÄM 7261) — the only true small bilingual (Egyptian throne name + Meroitic birth name); no downloadable transliteration found.

## Counts at a glance

| Layer | Size | Status |
|---|---|---|
| Real Meroitic phrases (Otten sources) | 871 | machine-readable, but no REM IDs |
| Augmented Meroitic sentences | 17,257 | synthetic, training only |
| Translated Meroitic words (Otten Table 1) | 193 | mostly names/titles/places |
| Words translatable with certainty (Rilly 2016) | ~100 | the gold set |
| Lexicon entries, graded (Rilly 2003 Vol. II) | ~800 | PDF scan, not structured |
| Transliterated texts (Hallof Vol. 7) | REM 0001-2780 + more | print only |
| Published texts in REM + appendices | ~1,300 | catalogue, scans only |
| Unpublished texts (mainly Qasr Ibrim, Musawwarat) | ~900 | not public |
| Comparative Swadesh lists (GLD) | Nubian 11, Tama 6, Nyimang 2 lects | PDF |
| Old Nubian records (DBMNT) | 4,518 texts | metadata, not full text |
| True bilingual texts | 1 (REM 0041, name-level) | no download |

## What this corpus can do

- Train cross-lingual embeddings (Meroitic vs Late Egyptian) on the Otten corpus, as Otten 2025 does.
- Test lexicon induction on the ~100 certain words and the 91-pair alignment dictionaries.
- Test a system on the three royal narratives as the only long, translated texts.
- Use funerary formulae (half the corpus) as a closed, repetitive test set.

## What it cannot do

- It cannot train a full translation model: there is no long bilingual text to learn from, and no held-out gold set exists yet.
- It cannot validate a claim about a new word: only ~100 words are certain, so most "translations" are proposals.
- It cannot use REM directly: REM is a catalogue of photos and descriptions, not text.
- It cannot use augmented lines as evidence: they are name-swapped copies of 871 real lines.

## First three build steps

1. Extract the ~100 certain words (Rilly 2016 + Rilly 2003 lexicon) as the gold test set; keep them out of training.
2. Parse the Otten corpus into per-line records with source tags (Millet / Rilly / Lobban / royal narrative), and mark every augmented line as synthetic.
3. Request or buy Hallof Vol. 7 (REM 0001-2780 transliterations) and Rilly 2003 Vol. II (PDF) as the real-text base; that is the step that changes the ceiling.
