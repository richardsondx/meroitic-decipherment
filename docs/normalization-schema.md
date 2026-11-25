# Normalization schema for REM transliteration

## Purpose

A single record format for every Meroitic text, so that REM catalogue entries, Hallof transliterations, the Otten corpus lines and the Rilly lexicon can be joined without silently mixing different kinds of data. Every field that is not known is left empty and flagged, never filled in by guesswork.

## 1. Sign inventory and Unicode

Meroitic is written with a 23-sign alphasyllabary plus a word divider.

- **16 basic syllable signs:** a, e, i, o, ya, ye, yi, yo, wa, we, wi, wo, ba, be, bi, bo (in the usual listing; the exact set is 4 vowels + 12 consonant+vowel syllables).
- **3 vocalic modifiers:** the signs that change a syllable's vowel (often written as a superscript or a following sign).
- **4 frequent syllables:** ne, se, te, to.
- **Word divider:** a sign separating words (two or three dots, or a short vertical stroke, depending on script and period).
- **Unicode (Unicode 6.1, January 2012):**
  - Meroitic Hieroglyphs: U+10980-U+1099F
  - Meroitic Cursive: U+109A0-U+109FF
  - ISO 15924 codes: Mero (hieroglyphic), Merc (cursive).
  - Unicode encodes more code points than the 23 signs (numerals, fractions, logograms, variants). Do not assume a one-to-one map between Unicode code points and the 23-sign inventory.
- **Font:** Noto Sans Meroitic (Google Fonts, SIL OFL 1.1, as reported).

## 2. Transcription convention (ASCII, Millet paradigm)

The Otten corpus and most scholarly work use an ASCII transcription. Normalise all incoming text to this before any modelling:

| ASCII | Meaning |
|---|---|
| a e i o | the four vowels |
| b d g k l m n p q r s t w y | consonants as in Millet |
| X | 4th h (h with a dot below in some editions) |
| x | 3rd h |
| S | s with a hat (š) |
| N | n with a tilde (ñ) |
| H | h with a tilde |
| E | e with a hat (ê) |
| : | word divider (normalised form; record the original divider shape in the metadata) |
| . | uncertain reading marker, as in the source (keep the source's notation; do not invent a new one) |
| [ ] | lacuna / restored text, as in the source |
| ( ) | editorial addition, as in the source |

Rules:
- Keep the source's transcription exactly in a `transcription_raw` field; put the normalised ASCII in `transcription_norm`.
- Never convert a proposed reading into a certain one. Uncertainty markers are data, not noise.
- Record the script (hieroglyphic / cursive) per text; the same sign can look different in the two scripts.
- Record the reading direction (right-to-left is normal for cursive; hieroglyphic follows the facing of the signs).

## 3. Tokenisation

- **Word:** a maximal string between word dividers. The divider is a token boundary, not a character.
- **Syllable:** a single sign (vowel, consonant+vowel, or modified syllable) is the atomic unit for character-level models. Do not split a sign into a consonant and a vowel; the sign is the unit.
- **Names:** royal names, theonyms and toponyms are single tokens; do not split them, and tag them as names (they are the most reliable alignments to Egyptian).
- **Numbers:** keep numeral signs as a separate token class; do not convert them to Arabic digits in the normalised text (record the Arabic value in a separate field if the edition gives one).
- **Formulae:** funerary formulae are highly repetitive; tag formulaic spans so a model cannot inflate its score by memorising them.

## 4. Record format (one JSON object per text)

```json
{
  "id": "REM 1044",
  "rem_number": "1044",
  "title": "Tanyidamani stela, Temple of Amun, Meroe",
  "site": "Meroe (Begrawiya)",
  "findspot": "Temple of Amun, Meroe",
  "support": "sandstone stela",
  "script": "cursive",
  "date": "c. 100 BCE",
  "date_earliest": -120,
  "date_latest": -80,
  "language": "Meroitic",
  "lines": 161,
  "transcription_raw": "...",
  "transcription_norm": "...",
  "translation": "...",
  "translation_status": "published | proposed | partial | none",
  "translation_source": "Rilly 2007 / FHN / Otten 2025",
  "genre": "royal narrative",
  "publication": "REM 1044; FHN 276-277",
  "images": ["persee_page_url_or_bm_object_url"],
  "provenance": "REM Vol. III / Hallof Vol. 7",
  "certainty_words": ["qore", "kdke", "..."],
  "notes": ""
}
```

Field rules:
- `id` is the REM number where one exists; otherwise use the publication reference (e.g. `MNL-29-1343`).
- `date_earliest` / `date_latest` are integers (negative = BCE). If the date is unknown, leave both empty and set `date` to "unknown".
- `translation_status` is one of four values only. "Published" means a scholarly translation exists in print; "proposed" means a gloss or partial reading; "partial" means only names/titles are translated; "none" means no translation.
- `certainty_words` lists only words translatable with certainty (the ~100-word set); never list a proposed gloss here.
- `images` holds URLs only; do not embed image files.

## 5. Lexicon record format (one JSON object per word)

```json
{
  "form": "qore",
  "form_norm": "qore",
  "gloss": "king",
  "gloss_status": "certain | proposed | rejected",
  "pos": "noun",
  "attestations": ["REM 1044", "REM 1003"],
  "cognates": [
    {"language": "Nobiin", "form": "ur", "source": "Rilly 2010:59", "status": "proposed"}
  ],
  "proto_form": "*kur",
  "proto_status": "reconstructed",
  "source": "Rilly 2003 Vol. II, s.v. qore",
  "notes": ""
}
```

- `gloss_status` "certain" is reserved for the ~100 words Rilly 2016 says are translatable with some certainty.
- `proto_form` is always a reconstruction; it is never an attestation and must never be used as training text.

## 6. Parallel alignment format

For the rare cases where a Meroitic text and a known-language text refer to the same king, event or object:

```json
{
  "pair_id": "REM0041-barkstand",
  "meroitic_text": "REM 0041",
  "other_text": "Berlin AM 7261, Egyptian hieroglyphic throne name",
  "other_language": "Egyptian",
  "alignment_type": "name | same_object | same_event | same_genre",
  "alignment_note": "throne name in Egyptian, birth name in Meroitic; not a translation"
}
```

- `alignment_type` must be one of the four values. There is no "translation" alignment type for Meroitic: no long bilingual translation exists.
- The Gallus stele, Silko and the Ezana Stone are `same_event` or `same_genre`, never `translation`.

## 7. What not to normalise away

- Do not merge hieroglyphic and cursive forms of the same text into one record; keep them as separate witnesses.
- Do not drop the word divider; it is the only word-boundary signal in the script.
- Do not expand abbreviations or restore lacunae without marking them.
- Do not treat the Otten augmented lines as texts; tag them `source: "otten-augmented"` and keep them out of any evaluation set.
- Do not mix reconstructed proto-forms into the Meroitic text corpus; they belong in the lexicon's `proto_form` field only.
