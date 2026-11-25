# Meroitic decipherment datasets — ranked inventory

Checked 2026-11-19/20. Every URL below was checked by the coordinator with `curl` HEAD/GET or `browser.open` unless marked "reported, not re-checked". Counts, licences and formats are only stated where a source stated them. "Not verified" means not found in the sources checked, not that it does not exist.

Rank order = value for building and validating a computational decipherment system. Primary transliterated text first.

## How to read the type labels

- **Primary transliteration** — Meroitic text rendered in Latin transcription by a scholar, from the object.
- **Catalogue** — metadata, photos, facsimiles, bibliography; no transliteration.
- **Proposed translation** — a scholar's gloss for a Meroitic word or passage; a hypothesis, graded or ungraded.
- **Reconstructed form** — a starred proto-form (Proto-Nubian, Proto-NES, etc.); never an attestation.
- **Parallel text** — a text in a known language (Egyptian, Greek, Latin) related by king, place, event or genre; almost never a translation of the same text.

---

## Rank 1 — The only machine-readable Meroitic corpus

### 1. Otten & Anastasopoulos 2025 — Meroitic-Corpus (GitHub)
- **Exact title:** "Towards Ancient Meroitic Decipherment: A Computational Approach" (paper); repo "Meroitic-Corpus"
- **Authors:** Joshua Otten, Antonios Anastasopoulos, George Mason University
- **Venue:** Proc. Second Ancient Language Processing Workshop, NAACL 2025, pp. 208-219, 4 May 2025
- **Paper URL (verified, HTTP 200, 883,484 bytes, 12 pp.):** https://aclanthology.org/2025.alp-1.11.pdf
- **Repo URL (verified live, public, main, 4 commits, created 2024-05-14):** https://github.com/Joshua-Otten/Meroitic-Corpus
- **Format:** Plain text (.txt), ASCII transliteration in Millet's paradigm; Python code; Word2Vec embeddings (.txt)
- **Records (paper Table 1, verified in the PDF):** 193 translated Meroitic words; 897 Meroitic phrases; 302 Late-Egyptian complete texts; 708 scanned Nubian pages. Paper §5.2: 871 example texts/phrases before augmentation; after name-swapping augmentation 17,257 sentences/phrases, 782,761 words, 1,868 unique word forms. Egyptian: 1,729 unique types, 99,338 tokens.
- **Contents (verified by downloading and inspecting the repo, 5,504,851-byte zip):** `mero-corpus.txt` 18,090 lines / 756,028 tokens (the augmented corpus; lines are not labelled by text, and there are no REM IDs); `MilletExamples.txt` 1,447 lines; `RillyExamples.txt` 40 lines; `LobbanVocabList.txt` 200 lines; three royal narratives (`TanyidamaniNarrative.txt` REM 1044; `HamadabStelaOfAmanirenasNarrative.txt` REM 1003; `KalabshaMeroiticInscriptionOfKharamadoyeNarrative.txt` REM 0094); `Kalabsha_Millet.txt`; seven small Meroitic-Egyptian alignment dictionaries (nouns 26, names 18, numbers 15, verbs 14, titularies 9, adjectives/adverbs 6, prepositions 3; 91+ pairs total); Meroitic and Egyptian Word2Vec embeddings at dims 20/50/100/120.
- **Sources of the corpus (paper §4):** Lobban Jr vocabulary list (cited as 2021; no bibliographic record for a 2021 Lobban list was found — flag), Rilly 2007 example phrases, Millet 1968 example phrases, plus the three royal narratives (Hofmann 1998; Hägg 2000).
- **Coverage:** c. 300 BCE-450 CE, funerary formulae heavily represented; royal narratives are the long-text tail.
- **Licence:** not found. No LICENSE file in the repo. Public visibility is not a licence; confirm with the authors before reuse.
- **Access:** open GitHub, no key.
- **Machine-readability:** yes, the only one. Caveats: no per-text IDs, no metadata, augmented lines are synthetic (name-swapped), translations are mostly titles, names and place names.
- **Provenance:** peer-reviewed ACL paper; corpus hand-built from secondary transcriptions, not transcribed from REM directly.
- **Local copy:** `downloads/otten-meroitic-corpus/` and `downloads/otten-meroitic-corpus.zip`
- **Type:** primary transliterations (re-transcribed) + proposed translations (limited).

---

## Rank 2 — The lexicon and the transliteration volume (print/PDF, not structured)

### 2. Rilly 2003, EPHE thesis Vol. II — Lexique méroïtique (~800 words)
- **Exact title:** *Le méroïtique. Données grammaticales, lexicales, position linguistique. Vol. II. Lexique méroïtique*
- **Author:** Claude Rilly, EPHE, Paris-Sorbonne, 2003 (NNT 2003EPHE4068). LLACAN collection on HAL.
- **Landing page (verified):** https://inalco.hal.science/LLACAN/tel-04793700v1 (also https://hal.science/tel-04793700)
- **Direct PDF (verified HEAD HTTP 200, 123,648,388 bytes):** https://hal.science/tel-04793700v1/file/These%20Rilly%20EPHE%202003%20Vol%202%20Lexique%20meroitique.pdf
- **Format:** PDF scan, 117.76 MB per HAL. Text layer not verified.
- **Records:** about 800 entries, each with full bibliography; rejected glosses quarantined in an addendum "Gloses non retenues". Includes theonyms, toponyms, anthroponyms.
- **Licence:** not stated on the HAL page.
- **Access:** open access on HAL.
- **Machine-readability:** no (print scan, no CSV/TEI). Needs OCR + manual structuring.
- **Download status:** direct download from this sandbox is extremely slow (server drops the connection after ~200 s; resumed chunks reached 48,344,872 bytes, 39%, by 04:26 UTC 20 Nov 2026). File on disk is genuine PDF data but incomplete, so it is NOT copied into `downloads/`. Download it from a faster connection or via the browser.
- **Type:** proposed translations, graded, with critical apparatus. Only ~100 words are translatable "with some certainty" (Rilly 2016).

### 3. Hallof 2024 — Analytic Meroitic Dictionary, Vol. 7: Documents (transliterations REM 0001-2780)
- **Exact title:** Jochen Hallof, *Analytisches Wörterbuch des Meroitischen / Analytic Meroitic Dictionary*, Band 7: Dokumente / Volume 7: Documents. J.H. Röll, Dettelbach, 2024. SRaT Band 13.7. ISBN 978-3-89754-629-5.
- **Verification:** the publisher excerpt was downloaded and read (3,286,514 bytes, 23 pp., verified PDF). Its contents page states: "Inscriptions REM 0001 to REM 2780, pp. 1-260; Additional Inscriptions, pp. 261-309". Preface: "Der Dokumentenband listet die Transkriptionen aller meroitischen Texte auf, die für die Erstellung des Analytischen Wörterbuchs des Meroitischen (AWM) benutzt worden sind."
- **Excerpt URL (verified):** https://www.newbooks-services.de/MediaFiles/Texts/5/9783897546295_Excerpt_002.pdf
- **Format:** print book, 6 dictionary vols + 1 documents vol. Excerpt PDF only is free.
- **Records:** transliterations for REM 0001-2780 plus additional inscriptions. The wider counts (2,370 inscriptions, 23,900 words, 9,300 lexemes) were reported by a research agent from retailer/catalogue listings and are NOT independently verified here.
- **Licence/access:** commercial, © 2024 Verlag J.H. Röll; no open licence; no digital/open version found.
- **Machine-readability:** no. Print transliterations; structuring them is the single highest-value acquisition step after REM itself.
- **Type:** primary transliterations (Vol. 7) + proposed translations/cognates (Vols. 1-6).
- **Local copy:** `downloads/hallof-2024-excerpt.pdf` (excerpt only)

### 4. Rilly 2010 — Le méroïtique et sa famille linguistique (comparative core)
- **Exact title:** *Le méroïtique et sa famille linguistique*. Claude Rilly, Peeters, Leuven-Paris, 2010, 557 pp. Afrique et langage 14; SELAF 454. ISBN 978-9042922372.
- **Contents (per Lipiński 2011 review, verified PDF):** comparison of 43 Meroitic words (pp. 59-156); a further 200-word comparison; ~170 reconstructed Proto-Northern East Sudanic proto-forms plus morphology (pp. 420-529).
- **Access:** print, paywalled. No open full text found. The Internet Archive identifier `lexiquemeroitiq0000rill` given by Keenable returns 404 — not verified.
- **Review (verified, 598,983 bytes, 18 pp.):** http://journals.pan.pl/Content/82152/PDF/ROrient%202-11-7_Lipi%C5%84ski.pdf
- **Type:** reconstructed forms + proposed translations. Never present its reconstructions as attestations.
- **Local copy:** `downloads/lipinski-2011-review-rilly2010.pdf` (review only)

### 5. Rilly & de Voogt 2012 — The Meroitic Language and Writing System
- **Authors:** Claude Rilly, Alex de Voogt. Cambridge University Press, 2012, 252 pp. ISBN 978-1-107-00866-3.
- **Contents:** history, phonology, grammar, affiliation; glossary pp. 183+; appendix pp. 189-230 with the 200 comparative terms and reconstructions; paleographic tables.
- **Access:** paywalled at Cambridge Core (https://www.cambridge.org/core/books/meroitic-language-and-writing-system/D1534C93DCCA955D82E0594CE92598FC). A full-book PDF circulates on Internet Archive (identifier `the-meroitic-language-and-writing-system-claude-rilly-alexander-j-de-voogt_202306`); its provenance/legality is not verified, so treat it as an unauthorised copy, not an open-access source.
- **Verified download (5,277,785 bytes, 266 pp.):** https://ia600608.us.archive.org/4/items/the-meroitic-language-and-writing-system-claude-rilly-alexander-j-de-voogt_202306/The%20Meroitic%20language%20and%20writing%20system%20%28Claude%20Rilly%20Alexander%20J%20de%20Voogt%29%20.pdf
- **Type:** proposed translations + reconstructed forms (appendix).
- **Local copy:** `downloads/rilly-de-voogt-2012-ia.pdf`

---

## Rank 3 — The REM corpus itself (catalogue, print + scans)

### 6. Répertoire d'épigraphie méroïtique (REM), Leclant et al., 2000, Vols I-III
- **Exact title:** *Répertoire d'épigraphie méroïtique. Corpus des inscriptions publiées*
- **Editors:** Jean Leclant (dir.), André Heyler, Catherine Berger-el Naggar, Claude Carrier, Claude Rilly. Académie des Inscriptions et Belles-Lettres, Paris, 2000; diffusion De Boccard/Peeters. ISBN 2-87754-113-4. 3 vols, continuous pagination XXII-715, 716-1371, 1372-2083.
- **Counts:** Vol. I REM 0001-0387 (714 pp.); Vol. II REM 0401-0851; Vol. III REM 1001-1278, plus 4 image catalogues and 4 indexes. Total published in REM + Carrier appendices (2000-2003): about 1,300 texts (Rilly 2016, verified). About 900 more unpublished, mainly Qasr Ibrim and Musawwarat (Rilly 2016). All known texts: "approximately 2,200" (Otten 2025) — treat as an estimate, not a reconciled count.
- **Contents per text:** facing pages, photo/facsimile, description, bibliography, location, support. **No transliteration in Vols I-III** — that was planned for Vols IV-VI, which have no publication record found (announced as in preparation c. 2000-2002).
- **Supplements:** Carrier, *Meroitic Newsletter* 27-30 (2000-2003), REM 1279-1367+ (e.g. REM 1343-1367 in MNL 29; REM 1368-1379 and REM 0023F in MNL 30).
- **Access:** print, 124 euros for 3 vols (AIBL). Free to read as scanned page images on Persée (see below). No TEI/CSV/API found.
- **Persée (verified live):** Vol. I issue https://www.persee.fr/issue/rem_0000-0000_2000_num_1_1 ; Vol. II doc https://www.persee.fr/doc/rem_0000-0000_2000_num_2_1_847 (HTTP 200); Vol. III doc https://www.persee.fr/doc/rem_0000-0000_2000_num_3_1_849 ; general contents https://www.persee.fr/doc/rem_0000-0000_2000_num_1_1_841 (opened and read; it is the Sommaire général, with the full chapter/REM-range table). Persée serves page images (renderPage JPGs); **no direct PDF download URL was verified** (the `/doc/{id}/{id}.pdf` pattern returns 404 for Vols I and III). Bulk download not verified.
- **Purchase pages (verified):** Vol. I https://aibl.fr/publications/repertoire-depigraphie-meroitique-vol-i/ ; Vol. II https://aibl.fr/hors-collections/repertoire-depigraphie-meroitique-vol-ii/ ; Vol. III https://aibl.fr/hors-collections/repertoire-depigraphie-meroitique-vol-iii/ (HTTP 200).
- **Machine-readability:** no. Page images only. Otten 2025: "the texts from REM are image files, and hence not amenable for text-based language technologies."
- **Type:** catalogue.
- **Related:** early computer work (Leclant 1972; Heyler 1970/74; Meeks CV note "1971-1972: Work on a meroitic texts database") — no surviving file, format or download found.

### 7. Trismegistos Texts — REM-based metadata (paywalled)
- **Institution:** Trismegistos, KU Leuven / Univ. Antwerp. https://www.trismegistos.org/
- **Coverage (reported):** "almost all Meroitic inscriptions based on Leclant, REM (2000)"; 945 texts on 24 Nov 2014; language table snapshot: Meroitic cursive 910 texts, Meroitic glyphs 90 texts. Dates of snapshots differ; do not present either as current.
- **Contents:** metadata only (date, provenance, material, script, publication = REM number). Example records state "We currently do not have a full-text version of this source."
- **Access:** paywalled since 1 Jan 2020; full function for registered users only; lists restricted to first 5 entries. Single-user 199 EUR incl. VAT if the institution does not subscribe (49 EUR if it does); institutional 299 EUR excl. VAT (per Trismegistos registration FAQ, as reported by a research agent; not re-checked live).
- **Licence:** content CC BY-SA per Trismegistos terms of use (as reported); database owned by KU Leuven.
- **Machine-readability:** no public API verified; subscription web UI only.
- **Type:** catalogue/index.

---

## Rank 4 — Parallel-text sourcebooks (known-language side)

### 8. Fontes Historiae Nubiorum (FHN) I-IV, 1994-2000
- **Exact title:** *Fontes Historiae Nubiorum: Textual Sources for the History of the Middle Nile Region between the Eighth Century BC and the Sixth Century AD*. Eds. Eide, Hägg, Pierce, Török, Univ. Bergen. Vol. I 1994 (343 pp., ISBN 82-991411-6-8); Vol. II 1996 (pp. 345-745); Vol. III 1998 (pp. 751-1216); Vol. IV 2000 (pp. 1217-1375).
- **Contents:** original language + new English translation + historical commentary per source (Egyptian, Demotic, Greek, Latin, Coptic, Meroitic). Meroitic entries give transliteration but **no consecutive translation**. Key numbers: Gallus FHN 164-165; Yesebokheamani FHN 276-277; Kharamadoye FHN 300; Esmetakhon FHN 306; Isemne FHN 311; Silko FHN 317.
- **Verified download — Vol. I full text (666,717 bytes, 21,991 lines, verified):** https://archive.org/download/romaindavid4_hotmail_FHNI/FHN%20I_djvu.txt (identifier `romaindavid4_hotmail_FHNI`)
- **Vols II-III:** Royal Holloway repository URLs given by a research agent do NOT resolve to the FHN PDFs via curl (empty reply) and the FHN III URL opens a **book review** of FHN III, not the volume. Yumpu hosts Bergen scans (viewer only, e.g. https://www.yumpu.com/en/document/view/48029080/-i-i-i-digitalt-universitetsbiblioteket-i-bergen-universitetet-i-bergen/16). No verified bulk PDF for Vols II-IV.
- **Licence:** © Klassisk institutt, Universitetet i Bergen, 1994. No open licence stated on the copies found.
- **Machine-readability:** partial (Vol. I as OCR DJVU text; imperfect OCR).
- **Type:** parallel text (known-language side) + primary Meroitic transliterations.
- **Local copy:** `downloads/fhn-vol1-djvu.txt` (Vol. I only)

### 9. Griffith 1911-1912 — Meroitic Inscriptions, Parts I-II (public domain)
- **Author:** F. Ll. Griffith. Part I (1911, 19th Memoir); Part II: Napata to Philae and Miscellaneous (1912, 20th Memoir, 48 plates). Also *Karanòg* (1911).
- **Contents:** primary transliterations, hand copies, photos, squeezes; the decipherment baseline. Karanog/Shablul material later re-catalogued as REM 0201-0387.
- **Verified download — Part II full text (300,715 bytes, 12,230 lines):** https://archive.org/download/archaeologicals20egyp/archaeologicals20egyp_djvu.txt
- **Access:** public domain, Internet Archive. OCR quality low.
- **Machine-readability:** low (OCR of early print with hand-drawn signs).
- **Type:** primary transliterations.
- **Local copy:** `downloads/griffith-1912-meroitic-inscriptions-II-djvu.txt`

### 10. The small bilingual and the Greek neighbours (no single download)
- **Wad Ben Naga bark stand, REM 0041, Berlin ÄM 7261** — the only true small bilingual: throne name in Egyptian hieroglyphs, birth name in Meroitic hieroglyphs (Natakamani/Amanitore, mid-1st c. AD). Berlin page verified HTTP 200: https://www.egyptian-museum-berlin.com/c33.php . No downloadable transliteration on that page. Note an inventory-number conflict: SARS Sudan & Nubia 27 calls it Inv. 7216 in one passage vs 7261 elsewhere — unresolved.
- **Gallus trilingual stele, Philae, 29 BC (OGIS 654; FHN 164-165; Cairo CG 9295)** — Egyptian/Latin/Greek, NOT Meroitic, but the only trilingual naming a Meroitic king. Full text verified: https://www.attalus.org/docs/ogis/s654.html (301 to https, HTTP 200). The hieroglyphic version is not a translation of the Latin/Greek.
- **Silko inscription, Kalabsha, Greek only (FHN 317)** — full English translation in *Meroitic Newsletter* 24: http://meroiticnewsletter.org/MeroNews24.pdf (reported; not re-checked live — the meroiticnewsletter.org host returns a Cloudflare challenge to curl, see §13).
- **Kharamadoye, REM 0094 (FHN 300)** — Meroitic only, latest Meroitic text (c. 410-450 CE), dated by Greek neighbours (Isemne FHN 311, Silko FHN 317). No standalone open dataset; refit in the Otten corpus.
- **Ezana Stone, Aksum (Ge'ez/Sabaean/Greek)** — method model only, no Meroitic. https://en.wikipedia.org/wiki/Ezana_Stone
- **Type:** parallel text (name-level bilingual; same-event neighbours).

---

## Rank 5 — Comparative lexical datasets (Old Nubian, Nobiin, Nara, Taman, Nyima)

### 11. Global Lexicostatistical Database (GLD / Starling), East Sudanic section
- **Compiler:** G. Starostin and contributors, Russian State University for the Humanities.
- **Contents:** annotated 100-item Swadesh lists. Nubian: 11 lects (Old Nubian 75/100 slots filled, several under doubt; Nobiin; Dongolawi; Kenuzi; Dilling; Kadaru; Debri; Karko; Wali; Birgid; Midob). Tama: 6 lects (Tama, Erenga, Sungor, Miisiirii, Ibiri, Abuu Shaarib). Nyimang: 2 lects (Ama, Afitti). Nara: basic lexicon.
- **Verified download — Nubian PDF (926,761 bytes, 67 pp.):** https://starlingdb.org/new100/nub.pdf
- **Query pages:** the Starling CGI endpoints now redirect starling.rinet.ru to starlingdb.org, and on 2026-11-20 both curl and the browser fetch returned "Sorry, the server may be busy" / HTTP 400 for the Tama/Nyimang/Nara query URLs. The Keenable claim that these are "directly accessible, fully documented, machine-readable" is NOT confirmed by today's live check. Treat as live-but-flaky HTML-queryable, no bulk file verified except the Nubian PDF above.
- **Licence:** not verified. Format: PDF/HTML, not CLDF/CSV.
- **Machine-readability:** low in PDF form; underlying database is HTML-queryable.
- **Type:** attested forms + explicitly starred reconstructed proto-forms (keep separate).
- **Local copy:** `downloads/gld-nubian-swadesh-starostin.pdf`

### 12. ASJP (Lexibank/CLDF) v21
- **Title:** CLDF dataset derived from Wichmann et al.'s "ASJP Database" v21 (2025).
- **Repo (verified HTTP 200):** https://github.com/lexibank/asjp — CC-BY-4.0 (stated on README, as reported).
- **Statistics (whole dataset, as reported):** 11,540 varieties, 6,126 Glottocodes, 100 concepts, 568,820 lexemes; 40-item lists.
- **Coverage for this slice (as reported):** Nara, Dongolese Nubian, Kunuz Nubian, Afitti, Ama, Assangori/Sungor, Tama, Nobiin (36 forms in one ASJP-derived CLDF entry for Nobiin). Old Nubian: no ASJP entry found (extinct, not a living-language list).
- **Machine-readability:** high (CLDF Wordlist).
- **Type:** attested short lists, ASJP transcription.
- **Local copy:** none (clone the repo; per-language form counts were not individually verified).

### 13. Database of Medieval Nubian Texts (DBMNT) — Old Nubian
- **Director:** Grzegorz Ochała, University of Warsaw. Launched 2011.
- **URL (verified HTTP 200):** https://dbmnt.pcma.uw.edu.pl/ (guidelines: https://dbmnt.pcma.uw.edu.pl/guidelines/texts/)
- **Records:** Texts 4,518; Names 1,738; People 3,725; IM References 8,538 (per Digital Orientalist, May 2026).
- **Contents:** all medieval Nubian texts, 8th-15th c., in Old Nubian, Greek, Coptic, Arabic and others; provenance, location, support, date, genre, names, bibliography, photos where available. Transcriptions/translations are a long-term goal, not complete.
- **Format:** FileMaker Pro 16 relational database; web interface; export in XML, CSV, Excel; REST API and OAI-PMH via Trismegistos (as reported).
- **Licence:** CC BY 4.0 (as reported). A Zenodo record/DOI for the DBMNT data dump was claimed ("also available through Zenodo") but **no Zenodo record was found** in search — not verified.
- **Machine-readability:** yes, the most machine-readable Old Nubian resource found (metadata + names, not full text).
- **Type:** catalogue + primary texts (partial transcriptions).
- **Local copy:** none (use the web export/API; no dump was located).

### 14. Starostin 2017 + Rilly comparative tables (PDF, reconstructions)
- **Starostin, "Lexicostatistical Studies in East Sudanic I", *Journal of Language Relationship* 15/2 (2017), pp. 87-113** — reconstructed 50-item lists for Proto-Nubian, Proto-Tama, Nara; 100-item matrices. Reported URL: https://jolr.ru/files/%28217%29jlr2017-15-1-2%2887-113%29.pdf (not re-checked live).
- **Browne 1996, *Old Nubian Dictionary* (Peeters)** — the lexical authority for Old Nubian; print, no open PDF found.
- **Wiktionary appendices** (secondary, scrapeable HTML): Northern Eastern Sudanic reconstructions (from Rilly 2010:420-529) https://en.wiktionary.org/wiki/Appendix:List_of_Northern_Eastern_Sudanic_reconstructions ; Nara word list (from Rilly 2005) https://en.wiktionary.org/wiki/Appendix:Nara_word_list ; Nilo-Saharan word lists https://en.wiktionary.org/wiki/Appendix:Nilo-Saharan_word_lists . CC BY-SA (standard, not verified on the page).
- **Dotawo 7 (2020), Comparative Northern East Sudanic Linguistics** — open articles, not a dataset. Zenodo book PDF: https://zenodo.org/records/19848740/files/aa431454-40d3-42f5-8069-381a15789257_book.pdf (HEAD 200 earlier; direct download from this sandbox returned a Zenodo 403 "unusual traffic" page — rate-limited, not dead). Articles: Rilly, Personal Markers (DOI 10.5070/D67052246); Norton, Ama Verbs (DOI 10.5070/D67052247); Jakobi, Nubian Verb Extensions (DOI 10.5070/D67052248).
- **Type:** reconstructed forms (Starostin/Rilly/Wiktionary); attested dictionary (Browne, print).

### 15. Smaller comparative items (reported, not all re-checked)
- **Digital Old Nubian Corpus pilot (Miyagawa/van Gerven Oei)** — TEI XML pipeline, Stauros Text up to 800 words; repo `somiyagawa/DigitalOldNubianCorpus`; paper PDF https://github.com/somiyagawa/DigitalOldNubianCorpus/raw/refs/heads/main/JADH.pdf (reported, not re-checked). Pilot only.
- **Satzinger 2018, Short Archaeological Wordlist (English/Sudani Arabic/Nobiin)** — open PDFs, small thematic field list: https://homepage.univie.ac.at/helmut.satzinger/Texte/Arabic-Nobiin.pdf (reported, not re-checked).
- **Chan numerals / Numeralbank (CLDF)** — Nobiin 40 and 73 forms via CLDF Meta https://meta.clld.org/languages/nobi1240 (reported, not re-checked); Sungor numerals page https://lingweb.eva.mpg.de/channumerals/Sungor.htm (reported).
- **Rosetta Project Tama Swadesh List** — OLAC record http://olac.ldc.upenn.edu/item/oai:rosettaproject.org:rosettaproject_tma_swadesh-1 ; IA identifier `rosettaproject_tma_swadesh-1` (reported, not re-checked).
- **Hugging Face:** no dedicated dataset for Old Nubian, Nobiin, Nara, Tama or Nyima found. Incidental: `facebook/bouquet` lists Nobiin among translated languoids; no Nobiin subset size verified.
- **Not available as downloads:** Edgar 1991 Tama Group Lexicon (unpublished manuscript); Savà/Banti Nara dictionary and ~900-item Higir wordlist (unpublished as of 2018/2024); Stevenson/Bender 2000 Nyimang/Dinik 500+-item lexicon (journal only); Khalil 1996 Nobiin dictionary (print); Idris/Khalil ~18,000-word Nobiin dictionary (print, ~700 pp., as stated on artofnubia.com).

---

## Rank 6 — Images and metadata

### 16. British Museum Collection Online + SPARQL
- **Object pages (verified in search):** EA1581 stela, Faras (https://www.britishmuseum.org/collection/object/Y_EA1581); EA77948 ostracon, Argin (https://www.britishmuseum.org/collection/object/Y_EA77948); EA71848 ostracon, Qasr Ibrim (https://www.britishmuseum.org/collection/object/Y_EA71848); EA71847 ostracon (http://www.britishmuseum.org/collection/object/Y_EA71847); EA77946 Demotic ostracon (https://www.britishmuseum.org/collection/object/Y_EA77946); EA1 Prudhoe Lions (https://www.britishmuseum.org/collection/object/Y_EA1); Hamadab Stela EA1650, 42 lines (see Wikipedia; BM object page not re-checked).
- **Counts:** no Meroitic-only total stated. Collection Online overall: nearly 2 million records (2011 figure, dated).
- **API:** SPARQL endpoint https://collection.britishmuseum.org/sparql (HEAD returned an empty response from this sandbox; reported as the canonical machine-readable interface, "widely reported as intermittent"). No documented public REST/JSON API. IIIF is used by the museum's own viewer, not offered as a documented public API.
- **Licence:** most images CC BY-NC-SA 4.0 for non-commercial use; commercial via sales@bmimages.com (as reported from BM terms page). Object-record/metadata licence: not found — do not assume the image licence covers bulk metadata reuse.
- **Machine-readability:** partial (SPARQL, intermittent; HTML object pages).
- **Type:** catalogue + images.

### 17. Musawwarat Graffiti Archive (MPIWG / Humboldt)
- **URL (verified live via browser.open):** https://musawwaratgraffiti.mpiwg-berlin.mpg.de/graffiti/locations/sudan_collection
- **Contents:** open-access interactive archive of the Great Enclosure graffiti (several thousand; Meroitic in 131 graffiti + 5 from the Lion Temple, only 25 published per Rilly 2022). Languages: Meroitic, Greek, Latin, Old Nubian, Arabic, French, Provençal. Digilib zoom viewer; RTI tested 2011, planned for open access. Underlying FileMaker research database.
- **Licence:** described as open access; no explicit licence (CC or otherwise) found.
- **Machine-readability:** web database + viewer; no public API/IIIF/bulk download verified.
- **Related paper (verified, 658,426 bytes, 16 pp., CC BY 4.0):** Rilly 2022, "Graffiti for Gods and Kings", *Der Antike Sudan* 33, pp. 7-18, HAL hal-03956626, https://hal.science/hal-03956626v1 — file https://hal.science/hal-03956626v1/file/Graffiti%20for%20Gods%20and%20Kings%20%28with%20figs%29.pdf
- **Local copy:** `downloads/rilly-2022-musawwarat-graffiti-hal.pdf`

### 18. Sudan Virtual Museum (launched 1 Jan 2026)
- **URL (reported):** https://archeologie.culture.gouv.fr/soudan-museum/en (French: /fr). SFDAS / NCAM, with Louvre and Durham University.
- **Contents:** virtual reconstruction of the Sudan National Museum galleries as before the war; "more than 1,000 artefacts from the ancient Kingdom of Kush". Tour only; no dataset, API, IIIF or image download verified.
- **Contact for contributions (reported):** sudanvirtualmuseum[at]proton.me
- **Context:** Sudan National Museum, Khartoum (est. 100,000 objects) was looted/damaged in the 2023-2025 war; NCAM director Ghalia Garelnabi said in Mar 2025 that 90% of holdings were destroyed. No online catalogue verified.

### 19. SARS — Sudan Archaeological Research Society
- **URL (verified HTTP 200):** https://www.sudarchrs.org.uk/ ; about/contact https://www.sudarchrs.org.uk/about/
- **Contents:** annual peer-reviewed journal *Sudan & Nubia* (Vols 1-28, 1997-2024, open-access PDFs); monographs (e.g. Edwards 1998 *Gabati*); fieldwork archive (photos, negatives, transparencies, 1930s-1980s) — access by prior appointment for members only; no online image database verified.
- **Email (verified on official site):** SARS@britishmuseum.org
- **Type:** publications + archive (request-based).

### 20. Louvre, Berlin, Liverpool, Petrie (images, no bulk data)
- **Louvre:** collections.louvre.fr, 482,000+ entries; images not open access (free to browse, not to download/reuse); no Meroitic count or object list verified; no public IIIF/API verified.
- **Berlin Egyptian Museum:** bark stand ÄM 7261 and other Meroitic objects on https://www.egyptian-museum-berlin.com/c33.php (verified HTTP 200). No API/IIIF/downloadable transliteration verified.
- **Liverpool World Museum:** Natakamani statue fragment (https://www.liverpoolmuseums.org.uk/artifact/statue-of-king-natakamani-fragment) and Teriteqas stela (https://www.liverpoolmuseums.org.uk/artifact/stela-of-king-teiteqese) — reported, not re-checked.
- **Petrie Museum, UCL:** 6 objects with Meroitic inscriptions per Mnamon (not independently verified); no Meroitic-specific object URL verified.

---

## Rank 7 — Grounding papers (not datasets, but the authoritative counts and sign tables)

### 21. Rilly 2016, "Meroitic", UCLA Encyclopedia of Egyptology
- **Verified download (425,506 bytes, 12 pp.):** https://escholarship.org/content/qt3128r3sw/qt3128r3sw_noSplash_a34fb083e49c75f88724b4054bd16aaf.pdf
- **Key facts read from the PDF:** corpus in REM + appendices about 1,300 texts; about 900 unpublished; longest text REM 1044, 161 lines; half the published corpus is funerary; about 250 graffiti; 16 amuletic texts; about 70 ostraca; no more than about 100 words translatable with some certainty; latest text Kharamadoye REM 0094, re-dated 410/450 CE.
- **Local copy:** `downloads/rilly-uee-2016-meroitic.pdf`

### 22. Rilly 2022, "Meroitic Writing", UCLA Encyclopedia of Egyptology
- **Verified download (2,365,242 bytes, 6 pp.):** https://escholarship.org/content/qt2ts0n9p0/qt2ts0n9p0.pdf
- **Contents:** 23-sign alphasyllabary, word-divider, hieroglyphic/cursive tables.
- **Local copy:** `downloads/rilly-uee-2022-writing.pdf`

### 23. Rilly 2008 (arXiv) and 2011 (ITYOPIS); Rilly, "L'écriture méroïtique" (UNAM)
- **Rilly 2008, "The Meroitic language" (arXiv 0808.3616v3) — verified, 180,642 bytes, 10 pp.:** https://arxiv.org/pdf/0808.3616v3 — `downloads/rilly-2008-arxiv.pdf`
- **Rilly 2011, "Recent Research on Meroitic, the Ancient Language of Sudan", ITYOPIS 1 — verified, 418,773 bytes, 15 pp.:** http://www.ityopis.org/Issues-1_files/ITYOPIS-I-Rilly.pdf — `downloads/rilly-2011-ityopis.pdf`
- **Rilly, "L'écriture méroïtique" (UNAM) — verified HEAD 200, 1,160,753 bytes, 13 pp.:** https://pueaa.unam.mx/uploads/materials/Rilly.pdf?v=1628639380 — `downloads/rilly-ecriture-meroitique-unam.pdf`

### 24. Smith 2007, Zipf plot of Meroitic (Glottometrics 15, pp. 53-61)
- **Verified download (1,669,985 bytes, 11 pp.):** http://meroiticnewsletter.org/meroiticpaper.pdf
- **Contents:** word-frequency counts for REM 1003 and combined REM 1001/1003/1044; top-20 ranked words. Statistical, not a corpus release.
- **Local copy:** `downloads/smith-zipf-2007.pdf`

### 25. Unicode / fonts (encoding, not language data)
- **Blocks:** Meroitic Hieroglyphs U+10980-U+1099F; Meroitic Cursive U+109A0-U+109FF (Unicode 6.1, Jan 2012). ISO 15924 Mero/Merc. Linguistic inventory: 23 signs + word-divider; Unicode encodes more code points for numerals, fractions, logograms and variants.
- **Proposal (Everson N3665, 2009):** https://escholarship.org/content/qt9gr6f43b/qt9gr6f43b.pdf?t=q4rj38 (reported, not re-checked).
- **Font:** Noto Sans Meroitic, Google Fonts, SIL OFL 1.1 (as reported; family page URL not verified verbatim).
- **Character notes:** https://r12a.github.io/scripts/merc/block.html (reported).

---

## Negative results (searched, not found — do not assume they exist)

- REM in TEI / CSV / JSON / database / API: not found. Print + Persée scans only.
- REM Vols IV-VI (transliterations): not found as published.
- Dedicated Meroitic dataset on Zenodo: not found (only Dotawo journal PDFs mention Meroitic).
- Dedicated Meroitic dataset on Hugging Face: not found (only incidental mentions).
- CLDF Meroitic wordlist/corpus: not found.
- DBMNT Zenodo dump record/DOI: not found (the "also available through Zenodo" claim has no locatable record).
- Rilly thesis Vol. I (grammar) on HAL: not found; only Vol. II confirmed.
- Millet 1968 dissertation open PDF: not found (UMI/ProQuest only).
- Lobban (2021) vocabulary list, bibliographic record/URL: not found.
- A Meroitic gold-standard / held-out benchmark: not found (see `benchmark-readiness.md`).
- Public IIIF endpoint for Meroitic inscriptions: not found.
- CNRS/LLACAN/EPHE dedicated Meroitic corpus portal: not found.
- OpenEdition Meroitic corpus: not found.
- FHN Vols II-IV as verified bulk PDFs: not found (Vol. I only, via IA; Vols II-III Royal Holloway URLs resolve to a book review / empty reply via curl).

## Keenable corrections (Keenable run https://app.keenable.ai/select/5c403712-b8cb-4c3e-8597-0b96909eafc3, 26m 55s, 13 queries, 2 failed)

Verified by the coordinator; see `keenable-verification.md` for the full audit. Headline corrections:
- De Gruyter DOI 10.1515/9783110892611 is NOT Rilly 2007 — it is Schleiermacher, "Vorlesungen über die Dialektik". Rilly 2007 is Honoré Champion, Paris.
- SARS Zach PDF and JSSEA_32.pdf links are both 404 (dead).
- Internet Archive `lexiquemeroitiq0000rill` is 404.
- HAL hal-03936546 does not exist in the HAL API (numFound 0); the /document URL is 404.
- DOI 10.5070/d61110040 could not be verified (empty 202 response).
- Starling CGI endpoints redirect to starlingdb.org and currently return "server may be busy" — not verified as serving data on 2026-11-20.
- Heidelberg Huber PDF is behind a bot-check page via curl.
- No "Rilly 2024 La langue méroïtique" title was found.
- Confirmed by the coordinator against Keenable: arXiv Rilly 2008 (verified); FHN Vol. I on IA (verified); Rilly & de Voogt 2012 on IA (verified, with the provenance caveat above); BM Images licensing via sales@bmimages.com.

## Verification log (coordinator, 2026-11-20, America/Toronto)

- HTTP 200 + byte counts confirmed for: ACL Otten paper; Otten GitHub repo + zip; HAL Rilly thesis HEAD; UEE 2016/2022; Smith 2007; arXiv Rilly 2008; IA Rilly & de Voogt 2012; ITYOPIS Rilly 2011; UNAM Rilly; Lipiński review; FHN I txt; Griffith 1912 txt; Hallof excerpt; HAL graffiti paper; GLD Nubian PDF; Persée REM Vol. II doc; AIBL Vol. III; SARS about page; Berlin museum page; Attalus Gallus; lexibank/asjp GitHub; DBMNT homepage.
- Blocked / failed: meroiticnewsletter.org (Cloudflare challenge to curl); SOAS Rowan thesis (403); Zenodo file downloads (403 "unusual traffic" from this sandbox IP); Royal Holloway repository (empty reply to curl); Starling CGI (server busy); HAL thesis full download (slow, 39% after 3 resumed rounds — see Rank 2); eScholarship without a browser User-Agent (0 bytes; works with one).
- Subagent reports (REM, lexicons, parallel/images, contacts) were recovered from their session transcripts and their URLs spot-checked as above; claims marked "reported" were not independently re-checked live.
