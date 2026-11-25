# Final report v2: Meroitic Decipherment v1.0

## Result

- The system explains known texts, but it cannot translate unseen ones.
- Exact-match accuracy runs 7.6 to 21.4 percent.
- Certain coverage runs 12.4 to 28.9 percent.
- Non-loan Certain coverage runs 9.8 to 24.5 percent.
- Unexplained tokens run 159 to 545 per narrative.
- The benchmark measures lexicon coverage, not prediction.
- The lexicon already cites each held-out text as evidence.
- Research infrastructure stands achieved.
- Decipherment stands incomplete.
- No claim in this report presents a proposal as certain.
- No reconstruction stands as an attestation.

## Evidence

- The corpus holds 460 texts and 5791 tokens.
- The tokeniser recomputes 5791 tokens, 0 mismatches.
- The corpus holds 0 synthetic lines.
- The lexicon holds 774 entries.
- 107 entries are certain, 664 are proposed, 3 are rejected.
- 19 certain entries are Egyptian loans.
- 88 certain entries are non-loan.
- The recompute script runs the source tokeniser and matcher.
- The script lives in the kit.
- Attestation leakage limits the blind test.
- REM 1044: 137 of 138 Certain tokens cite it.
- REM 1003: 136 of 139 Certain tokens cite it.
- REM 0094 FHN: 45 of 49 Certain tokens cite it.
- REM 0094 Millet: 82 of 86 Certain tokens cite it.
- Every exact token cites its own held-out text.
- A true blind test needs a text the lexicon never cites.
- No such text exists in the corpus yet.
- The Millet Witness mixes English glosses into the text.
- It holds 214 English-word tokens.
- 207 count as gap, 7 count as Certain.
- Cleaned Millet Certain coverage would be 16.5 percent.
- The headline scores stay as stored, uncleaned.

## Units

- U1 vocabulary gap: PASS, v4.
- U1 lists 715 gap types and 1535 gap tokens.
- U1 publishes the 80-word English list and the audit.
- U2 morphology: PASS, v3.
- U2 tests the top 50 gap forms.
- U2 proposes 10 hypotheses, 40 get no component found.
- U2 finds no root plus affix claim.
- U3 contextual tests: PASS, v3.
- U3 tests 27 candidates.
- U3 supports 7, refutes 4, leaves 16 untested.
- U3 labels every candidate proposed, never certain.
- U4 syntax: PASS, v4, after fix cycle 4.
- U4 finds 9 patterns, each with 3 to 14 examples.
- U4 cites each pattern from at least 3 distinct texts.
- U4 P3 cross-check is 29 records covering 28 distinct texts.
- U5 blind benchmark: PASS, md v2, json v3.
- U5 reports every required number per narrative.
- U5 shows no synthetic lines and no re-scoring.
- U5 shows the attestation limit plainly.
- U6 checker ran and passed U1, U2, U3, and U5.
- U6 checker failed U4 and the v1 report, narrowly.
- U6 judge ran and gave overall FAIL, narrowly.
- U6 judge passed U1, U2, U3, and U5.
- U6 judge failed one U4 P3 line and stale report lines.
- Fix cycle 4 corrected those lines.
- Fix cycle 4 fixes were checked by the coordinator only.
- No spawn was left for a fresh independent check of cycle 4.

## Kit

- Kit: Meroitic decipherment workbench kit, verified end to end on 2026-11-20.
- Path: ~/workspace/handover-meroitic-v1-2026-11-20/kits/meroitic-decipherment-workbench/
- The kit holds the recompute script and the format files.
- The command `python3 kits/meroitic-decipherment-workbench/recompute.py --u5` reproduces the scores.
- The command ran end to end on 2026-11-20, exit 0.
- The run reproduced the v3 narratives exactly, including every leakage field.
- The kit is no longer draft.

## Gaps

- Fixed: U1 English contamination is now reproducible.
- Fixed: the 80-word list and the audit script are published.
- Fixed: U2 affix count now reads 22, not 21.
- Fixed: U3 tmot inscription count now reads 3, not 4.
- Fixed: passive sentences are reworded in U2, U3, and U4.
- Fixed: long enumeration lines are split into vertical lists.
- Fixed: U5 attestation lists now use substring matching.
- Fixed: U4 P2 cross-check now reads 1 record, OTTEN-RILLY-003.
- Fixed: U4 P3 cross-check now reads 29 records, 28 distinct texts.
- Fixed: U4 te candidate now states the ends-with-te wording.
- Fixed: U1 and U4 stale pending lines are updated.
- Fixed: U5 md heading now reads v2.
- Queued: clean the Millet Witness into a new versioned file.
- Queued: add as to the English word list.
- Queued: align the unique-token definition with the source.
- Queued: find a text the lexicon never cites for a true blind test.
- Queued: check why REM 0012 holds 0 tokens.
- Queued: retest U4 patterns P3 and P4, both sit at the bar.
- Queued: resolve the 38 duplicate lexicon forms.
- Queued: one fresh independent check of the cycle 4 fixes, if approved.
- Accepted: U3-08 and U3-09 rest on one repeated formula.
- Accepted: their counts stand as distinct inscriptions, not as 20 evidences.
- Accepted: U3-05 repeats one phrase across 3 ids.
- Accepted: short lexicon forms stay untested by the matcher bar.

## Cost and envelope

- Cost spent: $0.00 of the $2.00 hard cap.
- No paid external model call ran.
- Fix cycles used: 4 of 5.
- Subagents used: 8 of 8.
- The run wrote only inside the run folder.
- The run edited no source file.
- The run sent no email and published nothing.
- The run bought nothing and deleted nothing.
- The run changed no acceptance rule.
- The run re-scored no held-out case.

## Next step

- Richardson decides the next move.
- Option one: approve the Rilly email draft.
- Option two: fund a cleaned Millet witness.
- Option three: seek Hallof Vol. 7 for new transliterations.
- Option four: seek a text the lexicon never cites.
- Option five: approve one fresh independent check of the cycle 4 fixes.
- The draft email sits at ~/workspace/meroitic-decipherment-datasets/draft-email-rilly.md.
- It is not sent.
- The first contact is Claude Rilly, claude.rilly@cnrs.fr.
