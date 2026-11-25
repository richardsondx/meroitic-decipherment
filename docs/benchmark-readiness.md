# Benchmark readiness

## Short answer

No. There is no held-out benchmark for Meroitic decipherment, and none can be built honestly until the REM transliterations exist in machine-readable form. What exists is a small set of certain words, three translated royal narratives, and one small alignment dictionary set. That is enough to test a method, not enough to certify a decipherment.

## What a benchmark needs, and what we have

| Requirement | Status |
|---|---|
| A held-out test set with known answers | Not available. Only ~100 words are translatable with certainty (Rilly 2016), and they are mostly names, titles and place names. |
| A long bilingual text to hold out | Does not exist. No Meroitic text has a consecutive translation in a known language. The only true bilingual (REM 0041 bark stand) aligns a throne name and a birth name, not sentences. |
| A transliterated corpus with IDs | Not available in machine-readable form. Hallof Vol. 7 (REM 0001-2780) is print only. The Otten corpus (871 real lines) has no REM IDs. |
| A train/dev/test split that does not leak | Not possible yet. The corpus is so small that any split leaks through formulaic funerary text. |
| A metric the field accepts | Not established. Otten 2025 uses intrinsic embedding evaluation and cross-lingual alignment, not a held-out translation test. |

## What Otten 2025 actually measured

- Cross-lingual lexicon induction (Meroitic to Late Egyptian) using the 91-pair alignment dictionaries and the embeddings.
- Result: 20% accuracy at best on **seen** terms, 0% on **unseen** terms (as reported by the contacts research agent from the paper; the paper is in `downloads/otten-2025-alp-1.11.pdf`).
- This is a baseline for a method, not a benchmark for a decipherment. Do not present it as one.

## Proposed hold-out design (once the data exists)

1. **Gold set:** the ~100 certain words (Rilly 2016 + Rilly 2003 lexicon, "certain" grade only). Keep them out of training entirely. Score: exact-match accuracy on these words, reported separately for names/titles vs common nouns vs verbs.
2. **Closed test set:** formulaic funerary texts (half the published corpus). Their repetition makes them the easiest test; report them separately so they cannot inflate the headline number.
3. **Long-text test:** the three royal narratives (REM 1044, REM 1003, REM 0094) as a held-out set, one at a time (leave-one-narrative-out). These are the only long translated texts.
4. **Alignment test:** the 91-pair Meroitic-Egyptian dictionaries, held out by category (nouns, names, numbers, verbs, titularies, adjectives/adverbs, prepositions).
5. **Proxy validation:** run the same pipeline on Ugaritic (Snyder et al. 2010) and Linear B, where gold answers exist, and report those numbers alongside the Meroitic numbers. A method that fails on Ugaritic has not been validated by succeeding on Meroitic.

## What leaks, and how to stop it

- **Name-swapping augmentation.** The Otten corpus's 17,257 sentences are name-swapped copies of 871 real lines. If augmented lines derived from the same source line land in both train and test, the test is contaminated. Fix: split by source line, before augmentation, and tag every augmented line.
- **Funerary formulae.** The same phrases repeat across hundreds of stelae. A random split puts near-identical texts on both sides. Fix: split by text (REM number), not by line, and report the formulaic subset separately.
- **Royal names and titles.** These are the easiest alignments and the most frequent. Fix: report them as a separate category; never let them dominate the score.
- **Egyptian loanwords.** Meroitic borrowed Egyptian words; a system that "translates" a loanword has not deciphered anything. Fix: tag loanwords and report them separately.
- **Proposed glosses presented as gold.** Most of the ~800 Rilly lexicon entries are proposed, not certain. Fix: only "certain"-grade entries may enter the gold set; "proposed" entries are training data at best, and must be labelled as such.

## What is gold vs proposed (the rule)

- **Gold:** the ~100 words translatable with some certainty (Rilly 2016); the three royal narratives' published translations; the Egyptian side of the 91-pair dictionaries (the Meroitic side is the thing being tested).
- **Proposed:** everything in the Rilly 2003 lexicon not marked certain; Hallof's dictionary glosses and cognates; Rilly 2010's reconstructions; any gloss from the Otten corpus that is not a name, title or place.
- **Reconstructed:** Rilly 2010's ~170 Proto-Northern East Sudanic forms; Starostin's proto-forms. Never use these as test answers.

## Models to copy for validation

- **Snyder, Barzilay & Knight 2010** (Ugaritic-Hebrew decipherment, ACL). Code/data: https://github.com/jluo93/NeuroDecipher (as reported).
- **Luo, Cao & Barzilay 2019**, "Neural Decipherment via Minimum-Cost Flow" (ACL 2019): +5.5% on Ugaritic, 67.3% cognates on Linear B.
- **Luo et al. 2021** (TACL): Gothic, Ugaritic, Iberian.
- **Frontiers in AI 2025** (three new Aegean benchmarks): https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1581129/full (as reported).

## Readiness verdict

| Stage | Ready? |
|---|---|
| Method prototyping (embeddings, alignment) | Yes — Otten 2025 shows it. |
| A train/dev/test split with a gold test set | No — needs Hallof Vol. 7 digitised and the ~100 certain words extracted. |
| A held-out translation benchmark | No — no long bilingual text exists. |
| A publishable decipherment claim | No — the data does not support one yet. |

## The first benchmark that can honestly be built

1. Digitise Hallof Vol. 7 (REM 0001-2780 transliterations).
2. Extract the ~100 certain words from Rilly 2003/2016 as the gold set.
3. Hold out the three royal narratives, one at a time.
4. Report: gold-word accuracy (by category), narrative word-accuracy, and the same pipeline's Ugaritic/Linear B numbers as a control.

Until step 1 is done, any "benchmark" is a method test on 871 lines, not a decipherment benchmark.
