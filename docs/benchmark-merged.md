# Merge and benchmark re-run, Nov 24, 2026

## Merge

- Old lexicon: 774 entries (107 certain, 664 proposed, 3 rejected).
- Rilly 2003 OCR lexicon: 744 entries (707 proposed, 37 rejected).
- Merged: 1,432 records, 1,387 distinct forms.
- Added new forms: 655. Merged into existing entries: 86. Second rejected records added: 3.
- Certain count unchanged at 107. No gloss status was upgraded.
- Status conflicts, all kept visible in the merge report:
  - ahide: old proposed, Rilly rejected section. Kept proposed, added rejected record.
  - dime: old proposed, Rilly rejected section. Kept proposed, added rejected record.
  - wi: old certain, Rilly rejected section. Kept certain, added rejected record.
- Duplicate forms in the new lexicon (ahide, dime, hr, mhe) kept as separate records, as the old lexicon does with its 38 duplicates.
- Rilly entries carry source_tag rilly-2003-vol2-lexicon, pdf_page, biblio, discussion, and permission_status academic-fair-use-excerpt. Loan status for Rilly entries is unassessed, not "not a loan".

## Benchmark, baseline to merged

- Method: same recompute script and matcher as U5, same 4 narratives, same tokeniser. Only the lexicon changed. Baseline files untouched.
- Certain coverage: unchanged on all 4 narratives. Exact-match accuracy: unchanged. This is expected, no new certain entries were added.

| Narrative | Certain | Exact | Proposed | Gap tokens |
| REM 1044 | 20.8% | 17.0% | 3.0% to 12.8% | 505 to 440 |
| REM 1003 | 28.9% | 21.4% | 3.3% to 11.9% | 326 to 285 |
| REM 0094 FHN | 21.3% | 11.3% | 9.6% to 29.1% | 159 to 114 |
| REM 0094 Millet | 12.4% | 7.6% | 8.9% to 12.8% | 545 to 518 |

- Gap tokens across the 4 narratives: 1,535 to 1,357, down 178.
- Gap unique types: 715 to 642, down 73.
- Proposed tokens matched: 1044 went 20 to 85, 1003 went 16 to 57, FHN went 22 to 67, Millet went 62 to 89.

## Leakage

- Certain tokens citing the held-out text: unchanged (137 of 138, 136 of 139, 45 of 49, 82 of 86).
- Lexicon entries citing each REM rose (44 to 73, 38 to 68, 27 to 88) because Rilly entries cite the narratives too.
- The benchmark still measures coverage of known texts, not prediction on unseen texts. The merge adds proposed glosses, not certain knowledge.

## What this means

- The lexicon nearly doubled, and the unexplained vocabulary shrank by 178 tokens.
- Certain coverage did not move, so the system still cannot translate an unseen inscription.
- The next step that would move certain coverage is contextual testing of the newly covered proposed forms (U3 method), starting with the 45 newly matched tokens in REM 0094 FHN and the 65 in REM 1044.

## Files

- lexicon-merged-v0.2.json: merged lexicon with counts.
- corpus/lexicon.json: same records as a bare list, as the recompute script reads it.
- merge-report.json: counts, conflicts, duplicates.
- recompute_merged.py: copy of the U5 recompute script, repointed at corpus/ and this folder.
- u5-benchmark-merged.json, u1-summary-merged.json, u1-gap-list-merged.json: re-run outputs.
- merge_lexicon.py: the merge script.
