# Missing data report

## What is missing, and why

### 1. A machine-readable REM corpus
- **Missing:** any TEI / CSV / JSON / database export of the ~2,000 Meroitic texts.
- **Why:** REM (Leclant et al. 2000) is a print catalogue of photos, facsimiles and descriptions. Its planned transliteration volumes (IV-VI) were never published, as far as any source found shows. Persée hosts page images only. No institution has released a text layer.
- **Impact:** this is the single blocker. Everything else is a workaround.

### 2. The REM transliteration manuscripts (Vols IV-VI)
- **Missing:** whether they exist at all, and where.
- **Why:** announced as in preparation c. 2000-2002; no publication record found in any catalogue searched.
- **Action:** ask Claude Rilly directly (see contacts).

### 3. The ~900 unpublished texts
- **Missing:** a list, let alone transliterations, of the unpublished texts, mainly from Qasr Ibrim and Musawwarat.
- **Why:** held by excavators and museums; Qasr Ibrim material is largely at the British Museum; Musawwarat graffiti are in the MPIWG/Humboldt archive, of which only 25 of 131+5 Meroitic graffiti are published.
- **Impact:** about 40% of the known corpus is invisible to any system.

### 4. A structured lexicon
- **Missing:** a machine-readable lexicon. Rilly 2003 Vol. II (~800 entries) is a 123.6 MB PDF scan; Hallof 2022-2024 (6 dictionary vols + documents vol) is print only.
- **Why:** both are print scholarship; nobody has structured them.
- **Action:** download the HAL PDF on a fast connection, OCR and hand-structure it; buy or request Hallof Vol. 7.

### 5. A gold-standard benchmark
- **Missing:** any held-out test set with known answers.
- **Why:** only ~100 words are translatable with certainty, and there is no long bilingual text to hold out. See `benchmark-readiness.md`.

### 6. Comparative datasets for the closest relatives
- **Missing:** a dedicated CLDF/Lexibank wordlist for Old Nubian, Nara, Tama or Nyima.
- **Why:** the data exists as PDFs, print dictionaries and unpublished manuscripts (Edgar 1991 Tama; Savà/Banti Nara; Stevenson/Bender 2000 Nyimang; Khalil 1996 Nobiin; Idris/Khalil ~18,000-word Nobiin dictionary), not as structured datasets. The best available are the Starling/GLD PDFs and ASJP CLDF 40-item lists.
- **Impact:** the cognate channel is thin and noisy.

### 7. Full-text Old Nubian
- **Missing:** a lemmatised Old Nubian corpus. DBMNT (4,518 texts) is metadata and names; transcriptions/translations are a long-term goal. The Digital Old Nubian Corpus pilot covers only a few texts (Stauros Text up to 800 words). ICON has 4 annotated texts / 125 words.
- **Why:** the field is small and the work is manual.

### 8. Open image data for inscriptions
- **Missing:** a bulk, openly licensed image set of Meroitic inscriptions with IIIF or an API.
- **Why:** the British Museum has the largest searchable set but no documented public REST API (SPARQL only, reported intermittent); the Louvre's images are not open access; the Sudan National Museum has no online catalogue and was looted in the war; the Sudan Virtual Museum is a tour, not a dataset; the Musawwarat archive has no bulk download.
- **Impact:** any vision/OCR work must scrape object pages or request access.

### 9. The "computerized Paris Repertoire"
- **Missing:** the early computer database of Meroitic texts worked on in Paris in the 1970s (Leclant 1972; Heyler 1970/74; Meeks CV note "1971-1972: Work on a meroitic texts database").
- **Why:** no surviving file, format or download was found. It may be lost, or held at LLACAN/EPHE without a public record.
- **Action:** ask Rilly/LLACAN.

### 10. Millet 1968 and Lobban 2021 sources
- **Missing:** an open PDF of Millet's 1968 dissertation (*The Meroitic Script and Language*) and any bibliographic record or URL for a 2021 Lobban vocabulary list (cited by Otten 2025).
- **Why:** Millet is UMI/ProQuest only; the Lobban citation could not be traced.
- **Impact:** the Otten corpus's two named sources cannot be re-checked from the open web.

## Institutional contacts (public pages only; no guessed addresses)

### Claude Rilly — the first contact
- **Role:** CNRS researcher, LLACAN; EPHE lecturer ("Langue et civilisation méroïtiques", 2025-26 programme).
- **Emails (verified on public pages):** claude.rilly@cnrs.fr (CNRS Fondation press release, 2018); claude.rilly@ephe.psl.eu (AOROC course listing, 2020-2021).
- **Profile:** https://www.ephe.psl.eu/claude-rilly (no email on the page, contact button only).
- **LLACAN:** 7 rue Guy Môquet, 94801 Villejuif, France. General email llacan.direction@cnrs.fr (as reported). Homepage https://llacan.cnrs.fr/ returned 403 via curl on 2026-11-20.

### SARS — Sudan Archaeological Research Society
- **Email (verified on official site):** SARS@britishmuseum.org
- **Site:** https://www.sudarchrs.org.uk/ (about page verified HTTP 200)
- **Treasurer (as reported):** annie.haward@spc.ox.ac.uk

### British Museum — Egypt and Sudan department
- **Keeper (as reported):** Daniel Antoine. Curators: Julie Renee Anderson, Loretta Kilroe. No individual staff emails found.
- **General:** communications@britishmuseum.org ; images sales@bmimages.com
- **Collection Online:** https://www.britishmuseum.org/collection ; SPARQL https://collection.britishmuseum.org/sparql

### Humboldt / MPIWG — Musawwarat Graffiti Archive
- **Archive:** https://musawwaratgraffiti.mpiwg-berlin.mpg.de/ (verified live)
- **Study advice (AKNOA, as reported):** studienfachberatung-aknoa@hu-berlin.de
- **Cornelia Kleinitz (archive lead):** no public email found.
- **Claudia Näser:** old email claudia.naeser@staff.hu-berlin.de (2007, unverified as current).

### Sudan
- **NCAM / Sudan National Museum:** no official email found.
- **Sudan Virtual Museum contact (as reported):** sudanvirtualmuseum[at]proton.me
- **NCAM director Ghalia Garelnabi Babiker:** only a personal Yahoo address from a 2018 report (unverified, do not use without checking).
- **Mohamed Bashir (Univ. of Khartoum archaeology, as reported):** mbashir@uni-muenster.de
- **SFDAS:** no current director/office email found. Vincent Francigny personal Gmail vfrancigny@gmail.com (2018, directorship ended 2019).

### INALCO
- No Meroitic-specific contact found; route via LLACAN / Rilly.

### DBMNT — Grzegorz Ochała
- **Role:** Chair of Epigraphy and Papyrology, University of Warsaw; DBMNT director since 2011.
- **Profile:** https://www.archeologia.uw.edu.pl/en/grzegorz-ochala-2/
- **DBMNT:** https://dbmnt.pcma.uw.edu.pl/

### Publishers
- **J.H. Röll (Hallof):** https://www.roell-verlag.de/ (not re-checked live)
- **AIBL (REM):** https://aibl.fr/ (purchase pages verified)

## What to ask each contact

- **Rilly / LLACAN:** Do REM Vols IV-VI exist in manuscript? Who holds the Qasr Ibrim / Musawwarat unpublished texts? Is there a digital REM database, and under what terms? Permission to structure the 2003 lexicon? Where is the 1970s Paris computer database?
- **AIBL / Persée:** bulk download or text layer for the REM scans; reuse licence.
- **J.H. Röll:** digital file or digitisation licence for Hallof Vol. 7 (and the dictionary vols).
- **British Museum / SARS:** Qasr Ibrim ostraca access; Collection Online bulk/API terms; fieldwork archive access.
- **MPIWG / Humboldt:** Musawwarat graffiti underlying data (FileMaker) and publication status of the 131+5.
- **Trismegistos:** subscription terms for the REM metadata index.
