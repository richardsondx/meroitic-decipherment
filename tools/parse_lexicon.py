#!/usr/bin/env python3
"""Parse Rilly 2003 Vol. II lexicon entries from OCR text into JSON.

Input: raw/page_NNN.tess.txt (tesseract, half-size) or raw/page_NNN.ocr.txt
(RapidOCR) for PDF pages 15-304. Lexicon proper: PDF pp. 15-279.
Rejected glosses ("Gloses non retenues"): PDF pp. 280-304.
Pages 1-14 are cover, intro, language glossary and one blank page.

Entry layout (verified by reading the page images):
- Headword line at the left margin, bold italic: e.g. "Adomn",
  "Adonili (var. Adenile)", "ahide (var. ahid)", "-/a/", "a-", "Abel".
  In the rejected section the headword is prefixed with "*": "*ab".
- Body: indented paragraphs. First line usually gives the part of speech
  in italic ("toponyme", "verbe (?)", "suffixe verbal", ...) and/or a
  French gloss in quotes, then discussion with REM citations.
- Each entry ends with a "Biblio. :" line of references.
- Letter sections open with a table of the letter's signs; those lines
  are not entries and are skipped.

Usage: python3 parse_lexicon.py
Writes rilly-2003-lexicon-v0.1.json and parse_log.txt in this folder.
"""
import json
import re
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"

LEX_START = 15
LEX_END = 279
REJ_START = 280
REJ_END = 304

POS_WORDS = [
    "substantif", "verbe", "adjectif", "adverbe", "pronom", "toponyme",
    "anthroponyme", "suffixe", "préfixe", "prefixe", "déterminant",
    "determinant", "copule", "particule", "interjection", "numéral",
    "numeral", "nom", "titre", "article", "conjonction", "préposition",
    "postposition", "locatif", "génitif", "négation", "démonstratif",
    "possessif", "ordinal", "cardinal", "pluriel", "singulier",
]
POS_RE = re.compile(
    r"^(" + "|".join(POS_WORDS) + r")", re.IGNORECASE)
REM_RE = re.compile(r"REM\s*0?(\d{3,4})(?:\s*/\s*(\d+))?")

# Words from the letter tables at the head of each letter section.
# They are not entries.
TABLE_WORDS = {
    "hieroglyphique", "hiéroglyphique", "cursive", "cursivearchaique",
    "cursivearchaïque", "cursivetardive", "archaïque", "archaique",
    "tardive",
}
QUOTE_RE = re.compile(r"[\"\u201c]([^\"\u201d]{2,120})[\"\u201d]")
BIBLIO_RE = re.compile(r"^Biblio\s*\.?\s*:", re.IGNORECASE)
VAR_RE = re.compile(r"\(var\.\s*([^)]+)\)")


def strip_diacritics(s: str) -> str:
    """Lowercase ASCII with combining marks removed. h-with-dot/line below
    both become plain h here; the millet mapping lives in form_millet."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("ø", "o").replace("đ", "d").replace("ł", "l")
    return s.lower()


def millet_norm(form: str) -> str:
    """ASCII in the Millet paradigm where the printed character is certain:
    š -> S, ñ -> N, ê -> E. The h-signs are NOT mapped here: the scans do
    not let OCR reliably tell h-with-dot-below from h-with-line-below,
    and guessing x vs X would corrupt the form. form_millet therefore
    keeps h as h; see the audit."""
    out = []
    for ch in form:
        if ch in "šŠ":
            out.append("S")
        elif ch in "ñÑ":
            out.append("N")
        elif ch in "êÊ":
            out.append("E")
        else:
            out.append(strip_diacritics(ch))
    return "".join(out)


def read_page_text(pdf_page: int):
    """Return OCR lines for a PDF page, tesseract first, RapidOCR fallback."""
    tess = RAW / f"page_{pdf_page:03d}.tess.txt"
    if tess.exists() and tess.stat().st_size > 0:
        return tess.read_text(errors="replace").splitlines(), "tesseract"
    ocr = RAW / f"page_{pdf_page:03d}.ocr.txt"
    if ocr.exists() and ocr.stat().st_size > 0:
        lines = []
        for ln in ocr.read_text(errors="replace").splitlines():
            parts = ln.split("\t", 1)
            if len(parts) == 2:
                try:
                    conf = float(parts[0])
                except ValueError:
                    conf = 1.0
                # drop low-confidence lines: mostly sign glyphs misread
                if conf < 0.75:
                    continue
                lines.append(parts[1])
            else:
                lines.append(ln)
        return lines, "rapidocr"
    return None, None


def is_headword(line: str, section: str) -> bool:
    """A headword line: starts at the left margin, short, word-like."""
    s = line.strip()
    if not s or len(s) > 45:
        return False
    if s.isupper():
        # section titles such as LEXIQUEMEROITIQUE are not entries
        return False
    if len(s) == 1:
        # lone letters come from the letter tables, not entries
        return False
    if s.lower().replace(" ", "") in TABLE_WORDS:
        return False
    if BIBLIO_RE.match(s):
        return False
    if s[0].isdigit():
        return False
    # rejected section: "*word"
    if section == "rejected":
        return bool(re.match(r"^\*[A-Za-zà-ÿḥḫḷṇṯšñê\-/]+(\s*\(var\..*\))?$", s))
    # main lexicon: word, optional (var. ...), or affix forms -/a/, a-, -te
    return bool(re.match(
        r"^[A-Za-zà-ÿḥḫḷṇṯšñê\*\-/]+(\s*\([^)]*\))?$", s)) and \
        not re.match(r"^(Voir|Dans|Le|La|Les|Ce|Cette|Il|Elle|On|Pour|Selon|"
                     r"Avec|Sans|Dans|Plus|Tout|Une?)\s", s)


def parse_entry(head: str, body_lines, pdf_page: int, section: str):
    """Parse one entry from its headword line and body lines."""
    rejected = section == "rejected" or head.startswith("*")
    form_raw = head.lstrip("*").strip()
    variants = []
    m = VAR_RE.search(form_raw)
    if m:
        variants = [v.strip() for v in m.group(1).split(",")]
        form_raw = VAR_RE.sub("", form_raw).strip()
    # affix forms keep their hyphens/slashes; plain words keep letters
    form = re.sub(r"\s+", " ", form_raw).strip()
    body = " ".join(ln.strip() for ln in body_lines if ln.strip())
    biblio = ""
    bm = re.search(r"Biblio\s*\.?\s*:\s*(.*)$", body, re.IGNORECASE)
    if bm:
        biblio = bm.group(1).strip()
        body = body[:bm.start()].strip()
    # part of speech: first word(s) of the body, if in the POS vocabulary
    pos = ""
    pm = POS_RE.match(body)
    if pm:
        pos = pm.group(1).lower()
        # two-word POS such as "suffixe verbal" / "préfixe verbal"
        m2 = re.match(r"^((?:suffixe|préfixe|pronom|nom)\s+\w+)", body, re.IGNORECASE)
        if m2 and len(m2.group(1).split()) == 2:
            pos = m2.group(1).lower()
    # gloss: quoted French strings in the body (Rilly's glosses are quoted)
    quotes = QUOTE_RE.findall(body)
    gloss = "; ".join(q.strip() for q in quotes[:3])
    # attestations: REM numbers cited in the body
    atts = []
    for rm in REM_RE.finditer(body):
        num = rm.group(1).zfill(4)
        att = f"REM {num}"
        if att not in atts:
            atts.append(att)
    return {
        "form": form,
        "form_norm": strip_diacritics(form),
        "form_millet": millet_norm(form),
        "gloss": gloss,
        "gloss_en": "",
        "gloss_status": "rejected" if rejected else "proposed",
        "pos": pos,
        "variants": variants,
        "attestations": atts,
        "biblio": biblio,
        "discussion": body,
        "pdf_page": pdf_page,
        "section": section,
        "source": f"Rilly 2003 Vol. II, s.v. {form}",
        "source_tag": "rilly-2003-vol2-lexicon",
        "permission_status": "academic-fair-use-excerpt",
        "gloss_language": "fr",
        "uncertain": False,
    }


def parse_pages(first=LEX_START, last=REJ_END):
    entries = []
    log = []
    for p in range(first, last + 1):
        lines, engine = read_page_text(p)
        if lines is None:
            log.append(f"page {p}: no OCR yet")
            continue
        section = "rejected" if p >= REJ_START else "lexicon"
        # drop the printed page number line (a lone number at top right)
        # and letter-table lines; keep the rest
        cur_head = None
        cur_body = []
        n_before = len(entries)
        for ln in lines:
            if ln.strip() == "":
                continue
            if ln.strip().isdigit() and len(ln.strip()) <= 3:
                continue
            if is_headword(ln, section) and cur_head is not None:
                entries.append(parse_entry(cur_head, cur_body, p, section))
                cur_head, cur_body = ln.strip(), []
            elif is_headword(ln, section):
                cur_head, cur_body = ln.strip(), []
            elif cur_head is not None:
                cur_body.append(ln)
        if cur_head is not None:
            entries.append(parse_entry(cur_head, cur_body, p, section))
        log.append(f"page {p} [{engine}]: {len(entries) - n_before} entries")
    return entries, log


def main():
    entries, log = parse_pages()
    out = {
        "version": "0.1.0",
        "source": "Rilly 2003, Le méroïtique. Vol II. Lexique méroïtique, "
                  "EPHE 2003, HAL tel-04793700, 304 pp.",
        "counts": {"entries": len(entries)},
        "records": entries,
    }
    with open(HERE / "rilly-2003-lexicon-v0.1.json", "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    with open(HERE / "parse_log.txt", "w") as f:
        f.write("\n".join(log) + "\n")
    print(f"entries: {len(entries)}")
    print("log lines:", len(log))


if __name__ == "__main__":
    main()
