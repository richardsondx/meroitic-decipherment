# Keenable verification audit

Keenable run: https://app.keenable.ai/select/5c403712-b8cb-4c3e-8597-0b96909eafc3
Status at handover: Complete, 26m 55s, 13 queries, 2 failed. No whole-report download button; only Copy table / Full table per table. Report renderer error noted on the page.
Checked by the coordinator on 2026-11-20 (America/Toronto). Each Keenable claim was checked live with curl HEAD/GET or browser.open before being used.

## Headline finding — confirmed

"No single downloadable machine-readable REM corpus was found. Only directly accessible, fully documented, machine-readable lexical data found are Starling Nubian, Taman, Nyima and Nara wordlists. Everything else is a book, PDF, index, museum API or institution request. REM itself is still not a public download. The ~2,000 texts estimate remains unverified as an exact current count."

Confirmed, with one correction: the Starling wordlists were **not** verified as serving data on 2026-11-20 (see Row 1-4). The headline conclusion stands; the "directly accessible" wording for Starling does not.

## Ranked inventory rows (14)

| Row | Keenable claim | Coordinator verdict |
|---|---|---|
| 1 | Starling Nubian etymological database, queryable HTML/CGI, no bulk file | **Partly confirmed, with a live failure.** The old starling.rinet.ru URLs 301-redirect to starlingdb.org. On 2026-11-20 the live CGI returned "Sorry, the server may be busy" in both curl and browser fetch. The underlying data exists as a PDF: https://starlingdb.org/new100/nub.pdf (verified, 926,761 bytes, 67 pp., downloaded). Licence not stated. |
| 2 | Starling Taman, 10 lists, ~110 concepts | **Not verified live.** Same server-busy failure as Row 1. The 10-list / ~110-concept counts come from the lexicons research agent and were not re-checked live. |
| 3 | Starling Nyimang, 10 lists, ~110 concepts | **Not verified live.** Same as Row 2. |
| 4 | Starling Nara group, two lists (Modern Nara, Old Nara), ~110 concepts, licence not stated | **Not verified live.** Same as Row 2. Licence not stated — confirmed (no licence found). |
| 5 | Rilly 2007, *La langue du royaume de Méroé*, De Gruyter DOI 10.1515/9783110892611 | **WRONG attribution.** The DOI resolves to Schleiermacher, "Vorlesungen über die Dialektik" (degruyterbrill.com, opened and read). Rilly 2007 is Honoré Champion, Paris; no De Gruyter DOI found. Do not cite this DOI for Rilly. |
| 6 | Rilly, *Le méroïtique et sa famille linguistique*, Internet Archive https://archive.org/details/lexiquemeroitiq0000rill | **Dead.** The identifier returns 404. Not verified. |
| 7 | Rilly 2012, same title, DOI 10.5070/d61110040 | **Not verified.** Browser fetch returned an empty 202 response; no PDF confirmed. |
| 8 | Rilly 2024, *La langue méroïtique*, PDF | **Not verified.** No such title found in search. Closest real items: Rilly 2019 CRAIBL "Où en est le déchiffrement du méroïtique" and the 2022 Collège de France lecture. |
| 9 | Zach 1992, *The Meroitic language*, SARS, https://www.sars.org.uk/wp-content/uploads/2023/02/SARS_SN21_Zach.pdf | **Dead.** 404. |
| 10 | Huber 2009, *Meroitic language*, Sudan & Nubia 13, Issuu https://issuu.com/sudarchrs/docs/s_n13_huber | **Viewer only.** Issuu is a page viewer, not a download. Not a machine-readable source. |
| 11 | Rilly 2008, *The Meroitic language*, arXiv https://arxiv.org/pdf/0808.3616v3 | **VERIFIED.** HTTP 200, 180,642 bytes, 10 pp., downloaded to `downloads/rilly-2008-arxiv.pdf`. |
| 12 | British Museum Collection online / BM Images, sales@bmimages.com | **Confirmed as described.** Museum API / image licensing, not a corpus download. Agrees with the parallel-texts research. |
| 13 | Fontes Historiae Nubiorum — authoritative editions/translations, no verified lawful bulk machine-readable file or segment alignment found | **Corrected.** FHN Vol. I IS on Internet Archive with full text: https://archive.org/download/romaindavid4_hotmail_FHNI/FHN%20I_djvu.txt (verified, 666,717 bytes, 21,991 lines, downloaded). Vols II-IV: no verified bulk PDF. |
| 14 | Musawwarat es-Sufra / HAL https://hal.science/hal-03936546/document | **Not verified; ID appears wrong.** The HAL API returns numFound 0 for that ID and the /document URL returns 404. The real Rilly 2022 Musawwarat graffiti paper is HAL hal-03956626 (verified, CC BY 4.0, downloaded). |

## Table 5 — verified direct PDF downloads

- Heidelberg Huber PDF (https://archiv.ub.uni-heidelberg.de/propylaeumdok/1141/1/Huber_Meroitic_Newsletter_32_2018.pdf): **blocked via curl** — returns a bot-check HTML page. Not verified as downloadable.
- JSSEA_32.pdf (https://www.sars.org.uk/wp-content/uploads/2024/10/JSSEA_32.pdf): **dead.** 404.
- arXiv Rilly 2008: verified (see Row 11).
- Zach / Issuu / De Gruyter: see Rows 9, 10, 5 — dead, viewer-only, wrong attribution.

## Other Keenable tables

- **Table 2 (REM acquisition):** needs REM 1-1000+ diplomatic transliterations, plus REM 1001, 1003, 1044A-D only after obtaining diplomatic editions from authoritative sources. Consistent with the coordinator's findings; the REM acquisition plan in this folder adds the Hallof Vol. 7 route (REM 0001-2780 transliterations, print, verified from the publisher excerpt), which Keenable did not surface.
- **Table 3 (comparative lexical, 10 rows):** no standalone bulk files verified — consistent with the coordinator's findings. The GLD Nubian PDF (starlingdb.org/new100/nub.pdf) is the one bulk file the coordinator did verify.
- **Table 4 (parallel/Napatan-Egyptian, 6 rows):** no aligned bilingual training set, only human-readable editions — confirmed.
- **Table 6 (images/metadata, 3 rows):** British Museum, SARS https://sudarchrs.org.uk/, licensed/request-based, not bulk — confirmed.
- **Table 7 (missing-data/benchmark):** no held-out benchmark exists, not ready, needs REM acquisition first — confirmed; see `benchmark-readiness.md`.
- **sources.tsv:** named in the Keenable text but no downloadable link was visible on the run page. Not recovered.

## What Keenable missed that the coordinator found

- Otten & Anastasopoulos 2025 and the GitHub Meroitic-Corpus (the only machine-readable Meroitic corpus) — the highest-value dataset in this investigation.
- Hallof 2024, Vol. 7 Documents (REM 0001-2780 transliterations in print).
- Rilly 2003 Vol. II lexicon on HAL (tel-04793700v1).
- FHN Vol. I on Internet Archive (full text).
- Griffith 1911-1912 on Internet Archive (full text).
- DBMNT (4,518 Old Nubian records, CC BY 4.0).
- ASJP CLDF coverage of Nara, Tama, Nyima, Nobiin.
- The Musawwarat Graffiti Archive as a live open-access resource.
- The correct HAL ID for the Rilly 2022 graffiti paper (hal-03956626, not hal-03936546).

## Method note

Keenable's run had 13 queries and 2 failed, and its report renderer showed an error. Its errors cluster in one pattern: plausible-looking links (a De Gruyter DOI, an IA identifier, a HAL ID, a SARS PDF path) that resolve to something else or to nothing. Every link in this inventory was re-checked live by the coordinator; the ones marked "not verified" above are the ones that failed that check.
