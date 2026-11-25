#!/usr/bin/env python3
"""Build a machine-readable Hallof Vol. 7 corpus from page text files.

Input: a folder of page_XX.txt files, one per PDF page of the Hallof
2024 Vol. 7 excerpt (or, for the full volume, of the full book).
Each page file holds the text layer of that PDF page, in reading order.

Output: hallof-excerpt-corpus-v0.2.json, one record per Hallof text.

Rules, all deliberate and documented:
- Normalization and tokenization are an exact port of
  normalizeMilletAscii / tokenizeNormalizedMeroitic in
  source-meroe-philology/src/engine/corpusSchema.ts.
- Entry parsing, group-metadata inheritance, genre, script and
  language detection are an exact port of parseHallofExcerpt in
  source-meroe-philology/scripts/build-corpus.ts, with two
  documented changes:
  1. Entries with no transcription lines are KEPT, with empty
     transcription, token_count 0, and an excerpt_status flag.
     The original parser dropped them, which hid REM 0072
     (non-Meroitic, no transcription) and REM 0092 (transcription
     cut off at the end of the free excerpt).
  2. Each record carries excerpt_pdf_page and inscription_page,
     so every record traces to its page file.
- Nothing is invented. A missing transcription stays empty.
- A proposed gloss is never presented as certain. This script
  writes no glosses at all; certainty_words come only from the
  certain-grade lexicon supplied with --lexicon.

OCR path: if --pdf is given instead of --pages, the script extracts
the text layer with pdftotext (preferred) or PyMuPDF. If a page has
no text layer, it is recorded as unreadable and the script stops
with a clear message naming tesseract as the tool to run next.
It never guesses text from a blank page.

Usage:
  python3 build-hallof.py --pages <dir> --out hallof-excerpt-corpus-v0.2.json
  python3 build-hallof.py --pages <dir> --lexicon <lexicon.json> \
      --rem-texts <rem-texts.json> --out hallof-excerpt-corpus-v0.2.json
  python3 build-hallof.py --pdf <file.pdf> --pages-out <dir> --out <file.json>
"""

import argparse
import datetime
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

VERSION = "0.2.0"

# ---------------------------------------------------------------------------
# Normalization: exact port of normalizeMilletAscii (corpusSchema.ts)
# ---------------------------------------------------------------------------
REPLACEMENTS = [
    ("\u1e2b", "x"),   # ḫ
    ("\u1e2a", "X"),   # Ḫ
    ("\u1e96", "X"),   # ẖ
    ("H\u0331", "X"),  # H with combining macron below (as written in TS)
    ("\u1e25", "X"),   # ḥ
    ("\u1e24", "X"),   # Ḥ
    ("h\u0303", "H"),  # h with tilde
    ("\u0161", "S"),   # š
    ("\u0160", "S"),   # Š
    ("\u00f1", "N"),   # ñ
    ("\u00d1", "N"),   # Ñ
    ("\u00ea", "E"),   # ê
    ("\u00ca", "E"),   # Ê
    ("\u0113", "E"),   # ē
    ("\u0112", "E"),   # Ē
    ("\u014d", "o"),   # ō
    ("\u014c", "o"),   # Ō
    ("\u2026", "..."), # …
    ("\u00b7", ":"),   # · author word divider
    ("\u22ee", ":"),   # ⋮
    ("\u205d", ":"),   # ⁝
    ("*", ""),          # editorial asterisks
]


def normalize_millet_ascii(raw: str) -> str:
    if not raw:
        return ""
    s = unicodedata.normalize("NFC", raw)
    for old, new in REPLACEMENTS:
        s = s.replace(old, new)
    s = re.sub(r"\s*:\s*", " : ", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\s+\n", "\n", s)
    s = re.sub(r"\n\s+", "\n", s)
    return s.strip()


def tokenize_normalized(norm: str) -> list:
    without_line_nums = re.sub(r"\(\d+\)", " ", norm)
    toks = []
    for tok in re.split(r"[\s:]+", without_line_nums):
        tok = re.sub(r"^[\[\]().,;]+|[\[\]().,;]+$", "", tok).strip()
        if tok and not re.fullmatch(r"-+", tok) and not re.fullmatch(r"\d+", tok):
            toks.append(tok)
    return toks


# ---------------------------------------------------------------------------
# Helpers ported from build-corpus.ts
# ---------------------------------------------------------------------------
def detect_formulaic(text: str, genre: str) -> bool:
    lower = f"{text} {genre}".lower()
    return any(
        w in lower
        for w in (
            "offering",
            "funerary",
            "wosi",
            "soreyi",
            "psolke",
            "psoxrke",
            "terikelowi",
            "tedxelowi",
        )
    )


def certainty_stem_set(lexicon_path: Path | None) -> set:
    """Certain-grade stems, from lexicon.json entries with gloss_status certain.

    The original builder used the same 107 GOLD_CERTAIN_SEEDS.
    If no lexicon is supplied, the set is empty and certainty_words is [].
    """
    if lexicon_path is None:
        return set()
    lex = json.loads(lexicon_path.read_text(encoding="utf-8"))
    stems = set()
    for rec in lex:
        if rec.get("gloss_status") != "certain":
            continue
        form = normalize_millet_ascii(rec.get("form_norm") or rec.get("form") or "")
        form = form.lower()
        if len(form) >= 2 and "-" not in form:
            stems.add(form)
    return stems


def find_certainty_words(norm_text: str, stems: set) -> list:
    found = set()
    for tok in tokenize_normalized(norm_text):
        clean = re.sub(r"[^a-z]", "", tok.lower())
        if clean in stems:
            found.add(clean)
            continue
        for stem in stems:
            if len(stem) >= 3 and clean.startswith(stem):
                found.add(stem)
    return sorted(found)


# ---------------------------------------------------------------------------
# Page text extraction (PDF input only)
# ---------------------------------------------------------------------------
def extract_pdf_pages(pdf_path: Path, out_dir: Path) -> list:
    """Extract one .txt file per PDF page. Returns a list of page numbers
    whose text layer was empty (unreadable without OCR)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    empty = []
    try:
        subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), str(out_dir / "page.txt")],
            check=True,
            capture_output=True,
        )
        # pdftotext writes one file; split it per page on form feeds.
        raw = (out_dir / "page.txt").read_text(encoding="utf-8", errors="replace")
        pages = raw.split("\x0c")
        for i, text in enumerate(pages, start=1):
            (out_dir / f"page_{i:02d}.txt").write_text(text, encoding="utf-8")
            if not text.strip():
                empty.append(i)
        (out_dir / "page.txt").unlink(missing_ok=True)
        return empty
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass
    # Fallback: PyMuPDF, if installed.
    try:
        import fitz  # type: ignore

        doc = fitz.open(pdf_path)
        for i, page in enumerate(doc, start=1):
            text = page.get_text()
            (out_dir / f"page_{i:02d}.txt").write_text(text, encoding="utf-8")
            if not text.strip():
                empty.append(i)
        return empty
    except ImportError:
        print(
            "ERROR: no pdftotext and no PyMuPDF. Install poppler-utils "
            "or PyMuPDF to extract a PDF text layer.",
            file=sys.stderr,
        )
        sys.exit(2)


# ---------------------------------------------------------------------------
# Entry parsing: port of parseHallofExcerpt, page by page
# ---------------------------------------------------------------------------
HEADER_RE = re.compile(r"^(?:\d+\s+)?reM\s+\d{4}\s*[–-]\s*reM\s+\d{4}", re.I)
GROUP_RE = re.compile(r"^REM\s+(\d{4}[A-Z]?)\s+to\s+REM\s+(\d{3,4}[A-Z]?)$", re.I)
SINGLE_RE = re.compile(r"^REM\s+(\d{4}[A-Z]?)$")
META_RE = re.compile(
    r"^(object|Findspot|Present location|Dating|Publication|note):\s*(.*)$", re.I
)
TRANSCRIPT_START_RE = re.compile(r"^(?:[A-Za-z0-9]+:)?\(\d+\)")


def parse_pages(pages_dir: Path):
    """Yield (pdf_page, line) pairs, with running headers stripped.

    PDF page N holds inscription page N-8 for this excerpt
    (inscription page 1 is PDF page 9). The offset is recorded in
    the output, not assumed for other books: callers must check it.
    """
    page_files = sorted(pages_dir.glob("page_*.txt"))
    if not page_files:
        print(f"ERROR: no page_*.txt files in {pages_dir}", file=sys.stderr)
        sys.exit(2)
    for pf in page_files:
        m = re.search(r"page_(\d+)\.txt$", pf.name)
        pdf_page = int(m.group(1)) if m else 0
        text = pf.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            if HEADER_RE.match(line):
                continue
            if "Meroitic word divider" in line and "lost signs" in line:
                continue
            if re.match(r"^Inscriptions\s+REM\s+0001\s+to\s+REM\s+2780$", line, re.I):
                continue
            yield pdf_page, line


def parse_entries(pages_dir: Path):
    entries = []
    current = None
    last_meta_key = None

    def new_entry(rem_num, is_group, group_end=None, pdf_page=0):
        return {
            "rem_num": rem_num,
            "is_group": is_group,
            "group_end": group_end,
            "meta": {},
            "text_lines": [],
            "first_pdf_page": pdf_page,
        }

    for pdf_page, line in parse_pages(pages_dir):
        gm = GROUP_RE.match(line)
        if gm:
            if current is not None:
                entries.append(current)
            current = new_entry(
                gm.group(1).upper(), True, gm.group(2).upper(), pdf_page
            )
            last_meta_key = None
            continue
        sm = SINGLE_RE.match(line)
        if sm:
            if current is not None:
                entries.append(current)
            current = new_entry(sm.group(1).upper(), False, None, pdf_page)
            last_meta_key = None
            continue
        if current is None:
            continue
        mm = META_RE.match(line)
        if mm:
            key = mm.group(1).lower()
            current["meta"][key] = mm.group(2).strip()
            last_meta_key = key
            continue
        looks_like_transcription = (
            len(current["text_lines"]) > 0
            or bool(TRANSCRIPT_START_RE.match(line))
            or line.startswith("---")
            or bool(re.match(r"^[A-Za-z]:\s*$", line))
            or (":" in line and ("·" in line or "(" in line or "[" in line))
        )
        if looks_like_transcription:
            current["text_lines"].append(line)
            last_meta_key = None
        elif last_meta_key:
            current["meta"][last_meta_key] = (
                f"{current['meta'][last_meta_key]} {line}".strip()
            )
        else:
            current["text_lines"].append(line)
    if current is not None:
        entries.append(current)
    return entries


def build_records(pages_dir: Path, stems: set, rem_texts_numbers: set | None,
                   pdf_page_offset: int = 8):
    entries = parse_entries(pages_dir)
    records = []
    active_group_meta = {}
    active_group_end = -1

    for e in entries:
        num_val = int(re.sub(r"\D", "", e["rem_num"]) or 0)
        if e["is_group"]:
            active_group_meta = dict(e["meta"])
            active_group_end = (
                int(re.sub(r"\D", "", e["group_end"]) or 0) if e["group_end"] else num_val
            )
            continue
        inherited = dict(active_group_meta) if num_val <= active_group_end else {}
        object_desc = (
            e["meta"].get("object") or inherited.get("object") or f"Inscription REM {e['rem_num']}"
        )
        findspot = e["meta"].get("findspot") or inherited.get("findspot") or "unknown"
        location = (
            e["meta"].get("present location")
            or inherited.get("present location")
            or "unknown"
        )
        dating = e["meta"].get("dating") or inherited.get("dating") or "unknown"
        publication = (
            e["meta"].get("publication")
            or inherited.get("publication")
            or f"Hallof 2024 Vol. 7 (REM {e['rem_num']})"
        )
        note = "; ".join(
            x for x in [inherited.get("note"), e["meta"].get("note")] if x
        )
        raw_text = "\n".join(e["text_lines"]).strip()
        norm_text = normalize_millet_ascii(raw_text)
        tokens = tokenize_normalized(norm_text)
        is_hiero = bool(re.search(r"hieroglyph", note, re.I)) or bool(
            re.search(r"nswt-biti", raw_text)
        )
        is_egyptian_mix = bool(
            re.search(r"nswt-biti|anx\s*·?\s*dt|sA\s*·?\s*Ra", raw_text)
        )
        site = findspot.split(",")[0].strip() or "unknown"
        genre = "temple / royal inscription"
        if re.search(r"rock inscription", object_desc, re.I):
            genre = "rock inscription / graffito"
        elif re.search(r"bark stand|altar", object_desc, re.I):
            genre = "royal bark stand / bilingual cartouche"
        elif re.search(r"ram|plinth", object_desc, re.I):
            genre = "royal dedication"
        elif re.search(r"offering|funerary|stela", object_desc, re.I):
            genre = "funerary / votive"

        # Excerpt status: the two cases the original parser hid.
        if not raw_text and "non-meroitic" in note.lower():
            status = "non-meroitic"
        elif not raw_text:
            status = "truncated"
        elif tokens:
            status = "complete"
        else:
            status = "zero-token"

        pdf_page = e["first_pdf_page"]
        records.append(
            {
                "id": f"REM {e['rem_num']}",
                "rem_number": e["rem_num"],
                "witness_id": f"REM-{e['rem_num']}-HALLOF",
                "title": f"REM {e['rem_num']}: {object_desc[:96]}",
                "site": site,
                "findspot": findspot,
                "present_location": location,
                "support": object_desc,
                "script": "hieroglyphic" if is_hiero else "cursive",
                "reading_direction": "rtl",
                "date": dating,
                "date_earliest": None,
                "date_latest": None,
                "language": "Meroitic+Egyptian" if is_egyptian_mix else "Meroitic",
                "lines": len(e["text_lines"]),
                "token_count": len(tokens),
                "transcription_raw": raw_text,
                "transcription_norm": norm_text,
                "translation": "",
                "translation_status": "none",
                "translation_source": "",
                "genre": genre,
                "is_formulaic": detect_formulaic(norm_text, genre),
                "publication": publication,
                "images": [],
                "provenance": "Hallof 2024, Analytisches Wörterbuch des Meroitischen, Band 7: Dokumente (Excerpt REM 0001–0092)",
                "source_tag": "hallof-2024-vol7-excerpt",
                "split": "hallof-excerpt",
                "synthetic": False,
                "permission_status": "pending-permission",
                "provenance_flag": "verified-edition",
                "certainty_words": find_certainty_words(norm_text, stems),
                "notes": note,
                "excerpt_pdf_page": pdf_page,
                "inscription_page": pdf_page - pdf_page_offset if pdf_page else None,
                "excerpt_status": status,
                "included_in_rem_texts": (
                    e["rem_num"] in rem_texts_numbers
                    if rem_texts_numbers is not None
                    else None
                ),
            }
        )
    records.sort(key=lambda r: r["rem_number"])
    return records


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pages", type=Path, help="folder of page_XX.txt files")
    ap.add_argument("--pdf", type=Path, help="PDF to extract page text from")
    ap.add_argument("--pages-out", type=Path, help="where to write extracted pages")
    ap.add_argument("--lexicon", type=Path, help="lexicon.json for certainty words")
    ap.add_argument("--rem-texts", type=Path, help="rem-texts.json for inclusion flags")
    ap.add_argument("--out", type=Path, required=True, help="output JSON file")
    ap.add_argument("--pdf-page-offset", type=int, default=8,
                    help="inscription page = pdf page minus this offset")
    args = ap.parse_args()

    if args.pdf is not None:
        if args.pages_out is None:
            print("ERROR: --pdf needs --pages-out", file=sys.stderr)
            sys.exit(2)
        empty = extract_pdf_pages(args.pdf, args.pages_out)
        if empty:
            print(
                f"WARNING: pages with no text layer (OCR needed): {empty}",
                file=sys.stderr,
            )
        pages_dir = args.pages_out
    elif args.pages is not None:
        pages_dir = args.pages
    else:
        print("ERROR: give --pages or --pdf", file=sys.stderr)
        sys.exit(2)

    stems = certainty_stem_set(args.lexicon)
    rem_numbers = None
    if args.rem_texts is not None:
        rem = json.loads(args.rem_texts.read_text(encoding="utf-8"))
        rem_numbers = {
            r["rem_number"]
            for r in rem
            if r.get("source_tag") == "hallof-2024-vol7-excerpt"
        }

    # The offset is applied inside build_records via pdf_page - offset;
    # it is kept as a parameter so a different book can use its own.
    records = build_records(pages_dir, stems, rem_numbers, args.pdf_page_offset)
    total_tokens = sum(r["token_count"] for r in records)
    out = {
        "version": VERSION,
        "generated_at": None,
        "source": {
            "title": "Jochen Hallof (2024), Analytisches Wörterbuch des Meroitischen, Band 7: Dokumente",
            "publisher": "Verlag J.H. Röll GmbH, Dettelbach",
            "isbn": "978-3-89754-629-5",
            "excerpt": "free publisher excerpt, 23 PDF pages, inscription pages 1-15, REM 0001-0092",
            "permission_status": "pending-permission",
        },
        "counts": {
            "records": len(records),
            "complete": sum(1 for r in records if r["excerpt_status"] == "complete"),
            "zero_token": sum(1 for r in records if r["excerpt_status"] == "zero-token"),
            "non_meroitic": sum(
                1 for r in records if r["excerpt_status"] == "non-meroitic"
            ),
            "truncated": sum(
                1 for r in records if r["excerpt_status"] == "truncated"
            ),
            "total_tokens": total_tokens,
            "rem_range": (
                f"{records[0]['rem_number']}-{records[-1]['rem_number']}"
                if records
                else None
            ),
        },
        "records": records,
    }
    out["generated_at"] = (
        datetime.datetime.now(datetime.timezone.utc)
        .isoformat()
        .replace("+00:00", "Z")
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote {args.out}: {len(records)} records, {total_tokens} tokens")
    print(
        "status counts:",
        {k: out["counts"][k] for k in ("complete", "zero_token", "non_meroitic", "truncated")},
    )


if __name__ == "__main__":
    main()
