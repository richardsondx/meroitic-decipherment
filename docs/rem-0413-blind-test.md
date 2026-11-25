# REM 0413 blind test

Merging means this: the text is now part of the corpus (rem-texts-v0.2.json, 461 texts) and it is scored as a held-out text the lexicon never cites.

## Result

- Total tokens: 8
- Certain coverage: 12.5% (1 of 8 tokens)
- Exact match (certain, exact mode): 12.5% (1 of 8 tokens)
- Proposed coverage: 0.0% (0 of 8 tokens)
- Gap tokens: 7 of 8 (87.5%)

## Token by token

| Token | Status | Mode | Matched form | Gloss |
|---|---|---|---|---|
| wbrxmlo | gap | - | - | - |
| ye | certain-native | exact | ye | optative / 3rd-person verbal prefix |
| sorli | gap | - | - | - |
| yinsidekeli | gap | - | - | - |
| nkeyi | gap | - | - | - |
| mkedokeli | gap | - | - | - |
| yinsidekeli | gap | - | - | - |
| nmlro | gap | - | - | - |

## Notes

- The lexicon cites REM 0413 in 0 entries, so the test is blind in the attestation sense.
- The token `ye` matches a certain entry by form only. The lexicon's certain glosses for `ye` are south/southern region and optative/3rd-person verbal prefix, not the personal-name suffix used here. Treat that one certain match with care.
- `sorli` (Osiris) does not count as certain. The lexicon holds `soreyi` as certain but bare `sor` only as proposed.
- Scored with the same tokenizer and matcher as the workbench recompute.py (port of tokenizeNormalizedMeroitic and matchToken from corpusSchema.ts), against lexicon-merged-v0.2.json.
- Translation is tentative (Elfiky 2025, after Hallof 2024 Vol. 7, 58). This test scores word coverage only. It does not test translation.
