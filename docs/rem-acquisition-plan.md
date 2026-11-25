# REM acquisition plan

## What REM is

*Répertoire d'épigraphie méroïtique. Corpus des inscriptions publiées*, edited by Jean Leclant (dir.), André Heyler, Catherine Berger-el Naggar, Claude Carrier and Claude Rilly. Académie des Inscriptions et Belles-Lettres, Paris, 2000. 3 volumes, continuous pagination to p. 2083, ISBN 2-87754-113-4.

## What is already digitised

- **Persée, free to read as scanned page images.** Vol. I issue: https://www.persee.fr/issue/rem_0000-0000_2000_num_1_1 ; Vol. II: https://www.persee.fr/doc/rem_0000-0000_2000_num_2_1_847 ; Vol. III: https://www.persee.fr/doc/rem_0000-0000_2000_num_3_1_849 ; general contents: https://www.persee.fr/doc/rem_0000-0000_2000_num_1_1_841 . All verified live 2026-11-20. Persée serves page images (renderPage JPGs). **No direct PDF download URL was verified** (the `/doc/{id}/{id}.pdf` pattern returns 404 for Vols I and III). No bulk download, no TEI, no API found.
- **Carrier appendices (REM 1279-1367+) in *Meroitic Newsletter* 27-30 (2000-2003)** — the newsletter's site (meroiticnewsletter.org) returns a Cloudflare challenge to curl, so no direct download was verified from this sandbox; PDFs are openly linked from the site and should be fetched in a browser.
- **Trismegistos metadata** — REM-based, 945 texts (2014 snapshot); metadata only, paywalled since 2020.

## What is print-only

- REM Vols I-III (AIBL, 124 euros for 3 vols; purchase pages verified: https://aibl.fr/publications/repertoire-depigraphie-meroitique-vol-i/ and https://aibl.fr/hors-collections/repertoire-depigraphie-meroitique-vol-iii/).
- Hallof 2024, *Analytic Meroitic Dictionary* Vols 1-7 (J.H. Röll). Vol. 7 Documents holds transliterations for REM 0001-2780 plus additional inscriptions (verified from the publisher excerpt, `downloads/hallof-2024-excerpt.pdf`). This is the single most valuable print acquisition: it is the closest thing to a machine-usable REM text.
- Rilly 2007, *La langue du royaume de Méroé* (Honoré Champion, Paris) — print; the De Gruyter DOI Keenable gave for it is wrong (it is Schleiermacher).
- Rilly 2010, *Le méroïtique et sa famille linguistique* (Peeters) — print.
- Rilly & de Voogt 2012 (Cambridge) — print; an IA copy exists but its provenance is not verified.
- Rilly 2003 thesis Vol. I (grammar) — not found on HAL; Vol. II (lexicon) is on HAL as a 123.6 MB PDF (see below).

## What needs scan, OCR, or a request

1. **REM Vols IV-VI (transliterations).** Announced as in preparation c. 2000-2002. No publication record found. Ask Claude Rilly / LLACAN whether they exist in manuscript or were abandoned. This is the first question for the first contact.
2. **The ~900 unpublished texts** (mainly Qasr Ibrim and Musawwarat, per Rilly 2016). These are held by excavators and museums; no public list was found. Qasr Ibrim material is largely at the British Museum; Musawwarat graffiti are in the MPIWG/Humboldt archive (see inventory Rank 6).
3. **Hallof Vol. 7 transliterations (REM 0001-2780).** Print only. Options: buy the volume (J.H. Röll), request a licence to digitise it, or ask the publisher for a digital file. This is the fastest path to a real transliterated corpus.
4. **Rilly 2003 Vol. II lexicon PDF** (123,648,388 bytes, HAL tel-04793700v1). Open access, but the HAL server is very slow from this sandbox (three resumed rounds reached only 39% by 04:26 UTC 20 Nov 2026). Download it from a fast connection or ask HAL/LLACAN for a copy. Once downloaded it still needs OCR + manual structuring (scan, ~800 entries).
5. **Persée page images.** If Persée's terms allow, harvest the page images and OCR them — but note REM's value is the photos/facsimiles and descriptions, not text; OCR of REM gives metadata and bibliography, not transliterations. Do not present OCR of REM as a transliterated corpus.
6. **Meroitic Newsletter back issues (PDFs).** Fetch in a browser from meroiticnewsletter.org; the site blocks curl with a Cloudflare challenge.
7. **FHN Vols II-IV.** Vol. I is downloaded (`downloads/fhn-vol1-djvu.txt`). Vols II-III Royal Holloway repository links do not resolve to the volumes via curl (the FHN III link opens a book review). Try the live browser, or Yumpu's Bergen scans (viewer only).

## Steps, in order

1. **Contact Claude Rilly (CNRS-LLACAN / EPHE) first.** He is the living authority and the likely holder or knower of the REM transliteration manuscripts. Verified public emails: claude.rilly@cnrs.fr (CNRS Fondation press release, 2018) and claude.rilly@ephe.psl.eu (AOROC course listing 2020-2021). Ask: (a) do REM Vols IV-VI exist in manuscript; (b) who holds the Qasr Ibrim / Musawwarat unpublished texts; (c) is there a digital REM database, and under what terms; (d) permission to structure the 2003 lexicon.
2. **Contact the AIBL / Persée** about the Persée REM scans: is there a bulk download or a text layer, and what licence covers reuse?
3. **Buy or request Hallof Vol. 7** (J.H. Röll, ISBN 978-3-89754-629-5) and the six dictionary volumes if budget allows.
4. **Download Rilly 2003 Vol. II** from HAL on a fast connection; OCR and structure the ~800 entries.
5. **Fetch the Meroitic Newsletter PDFs** (MNL 27-30, plus 24 for Silko) in a browser.
6. **Request Trismegistos access** (institutional subscription) for the REM-based metadata index, to reconcile counts.
7. **Contact the Musawwarat Graffiti Archive team** (Humboldt / MPIWG) about the 131+5 Meroitic graffiti and whether the underlying FileMaker data can be shared.
8. **Contact SARS** (SARS@britishmuseum.org) about the fieldwork archive and the Qasr Ibrim ostraca.

## Owners

- Rilly / LLACAN: REM transliterations, unpublished texts, lexicon permission.
- AIBL / Persée: REM scans and reuse terms.
- J.H. Röll / Hallof: Vol. 7 transliterations.
- British Museum / SARS: Qasr Ibrim material, object images.
- MPIWG / Humboldt: Musawwarat graffiti data.
- Trismegistos (KU Leuven): metadata index.

## Cost notes (as reported, not verified by purchase)

- REM 3 vols: 124 euros (AIBL).
- Trismegistos: single-user 199 EUR incl. VAT if the institution does not subscribe (49 EUR if it does); institutional 299 EUR excl. VAT.
- Hallof 7 vols: price not verified; check the J.H. Röll shop.
- Everything else in this plan is open access or request-based.
