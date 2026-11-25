# Contributing to Meroitic Decipherment

Thank you for helping. Meroitic is still partly undeciphered, and every new text or checked gloss moves the work forward. This page tells you what we accept, how to format it, and how we check it.

## What counts

We accept these kinds of contributions:

- **Primary transliterations.** A Meroitic text rendered in Latin transcription by a scholar, from the object. This is the most valuable kind.
- **Lexicon entries.** A Meroitic word with a gloss, part of speech, and attestations (REM numbers with line references).
- **Parallel texts.** A text in a known language (Egyptian, Greek, Latin) related to a Meroitic text by king, place, event, or genre. Say plainly if it is not a translation of the same text.
- **Images with metadata.** Photos, facsimiles, or drawings of an inscription, with findspot, present location, and publication reference.
- **Contextual tests.** A U3-style test of a proposed gloss across multiple independent inscriptions.
- **Corrections.** Errors in our corpus, lexicon, or reports, with a source citation.

We do not accept:

- Synthetic or name-swapped lines. The 17,257 augmented lines from Otten 2025 were quarantined for a reason.
- Reconstructed proto-forms presented as attestations. Mark every reconstruction as reconstructed.
- A gloss upgraded to certain without evidence. See the rule below.
- Scans or full text of a book that is still under copyright, unless the publisher or author gave written permission.

## The record format

Follow `docs/normalization-schema.md` for transcription, normalization, and tokenization. Follow `data/rem-0413.json` as the example record. A text record must have:

- `id`: the REM number, or a stable ID if the text has no REM number yet.
- `transcription_raw`: the transcription exactly as printed, with uncertain signs kept as printed.
- `transcription_norm`: the normalized form, following the schema.
- `token_count`: count tokens with the corpus tokenizer (see `tools/recompute.py`).
- `lines`: the number of lines.
- `site`, `findspot`, `present_location`, `support`, `script`, `date`, `language`, `genre`.
- `publication`: full citation of the source you took it from.
- `source_tag`: a short tag naming your source, for example `elfiky-2025-shedet-rem0413`.
- `permission_status`: `open-cc-by-4.0`, `open-cc-by-sa`, `academic-fair-use-excerpt`, `public-domain`, or `pending-permission`. Never write `open` for a source you have not checked.

A lexicon entry must have:

- `form`: the Meroitic form as printed.
- `form_norm`: the normalized form, lowercased.
- `gloss`: the proposed meaning, in English, with the source language if it came from a French or German text.
- `status`: `proposed` or `rejected`. Never `certain` in a new submission. See the rule below.
- `attestations`: a list of REM numbers with line references.
- `biblio`: the full citation for the gloss.

## The rule on certain

No gloss is ever upgraded to certain without independent evidence across multiple inscriptions. A gloss becomes certain only when:

- It fits in at least 3 decided inscriptions, counted the U3 way (the two REM 0094 witnesses count as one inscription).
- The evidence comes from more than one repeated formula.
- The proposer is not the only source of the evidence.

Until then, the gloss stays proposed, however plausible it looks. This rule is the reason the benchmark numbers are honest. Do not work around it.

## Check the license before you submit

- Find the license on the source page first. If the source page states no license, write `pending-permission` and say so in your pull request.
- Public visibility is not a license. A public GitHub repo with no LICENSE file is not open data.
- A free publisher sample (Leseprobe or excerpt) is a fair-use excerpt, not the whole book. Submit only the excerpt, with its source.
- If you are unsure, ask in an issue before you do the work. We would rather check first than delete your work later.

## Run the benchmark on a new text

If you add a text, check it against the benchmark before you submit:

1. Put your record in the format above and check it parses as JSON.
2. Run the tokenizer from `tools/recompute.py` on your text and confirm the token count.
3. List every token that matches a certain entry, a proposed entry, or nothing.
4. State the result in your pull request: how many tokens, how many certain, how many proposed, how many unexplained.
5. If the text is one the lexicon never cites, say so. That makes it a blind-test candidate, which is the most valuable kind of text we can get.

## Pull request checklist

Copy this list into your pull request and check each box:

- [ ] Every record follows the format in this file and parses as JSON.
- [ ] Every transcription is copied exactly as printed, with uncertain signs kept.
- [ ] Every gloss is marked proposed or rejected, never certain.
- [ ] Every source has a full citation and a permission status.
- [ ] No synthetic or augmented lines are included.
- [ ] No copyrighted full text is included without written permission.
- [ ] The token count was checked with the corpus tokenizer.
- [ ] If the text is new to the lexicon, the pull request says so and names it as a blind-test candidate.
- [ ] The README numbers were not changed, unless the pull request re-runs the benchmark and shows the new numbers.

## Questions

Open an issue first if your contribution is large, if the license is unclear, or if you are not sure a text is new. Small fixes (a typo, a wrong page number, a broken link) can go straight into a pull request.
