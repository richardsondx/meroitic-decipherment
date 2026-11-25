#!/usr/bin/env python3
"""Extract attestations for U3 retest candidates from rem-texts.json.

Ports tokenizeNormalizedMeroitic and clean_token from
merge-benchmark/recompute_merged.py (which ports corpusSchema.ts).
One occurrence per text is listed, with a window of surrounding tokens
and the stored translation. The two REM 0094 witnesses are flagged so
the retest can count them as one inscription per the U3 rule.
Read-only: reads the corpus, writes only the two output files named below.
"""
import json
import re
import sys
from pathlib import Path

RUN = Path(__file__).resolve().parents[2]
CORPUS = RUN / "source-meroe-philology" / "public" / "data" / "corpus"
OUT = Path(__file__).resolve().parent

FORMS = sys.argv[1:] if len(sys.argv) > 1 else []


def tokenize(norm):
    s = re.sub(r"\(\d+\)", " ", norm or "")
    out = []
    for tok in re.split(r"[\s:]+", s):
        tok = re.sub(r"^[\[\]().,;]+|[\[\]().,;]+$", "", tok).strip()
        if not tok:
            continue
        if re.fullmatch(r"-+", tok):
            continue
        if re.fullmatch(r"\d+", tok):
            continue
        out.append(tok)
    return out


def clean(raw):
    return re.sub(r"[^a-z]", "", raw.lower())


def main():
    texts = json.load(open(CORPUS / "rem-texts.json"))
    result = {}
    for form in FORMS:
        hits = []
        for t in texts:
            toks = tokenize(t.get("transcription_norm") or "")
            cleans = [clean(x) for x in toks]
            idxs = [i for i, c in enumerate(cleans) if c == form]
            if not idxs:
                continue
            windows = []
            for i in idxs:
                lo = max(0, i - 6)
                hi = min(len(toks), i + 7)
                windows.append(" ".join(toks[lo:hi]))
            hits.append({
                "id": t["id"],
                "rem_number": t.get("rem_number"),
                "witness_id": t.get("witness_id"),
                "split": t.get("split"),
                "occurrences": len(idxs),
                "windows": windows,
                "translation": t.get("translation") or "",
                "translation_status": t.get("translation_status"),
            })
        result[form] = hits
    json.dump(result, open(OUT / "attestations.json", "w"), indent=1, ensure_ascii=False)
    with open(OUT / "attestations.txt", "w") as f:
        for form in FORMS:
            hits = result[form]
            f.write(f"\n{'=' * 70}\n{form}: {len(hits)} inscriptions, "
                    f"{sum(h['occurrences'] for h in hits)} occurrences\n")
            for h in hits:
                f.write(f"\n[{h['id']}] split={h['split']} occ={h['occurrences']} "
                        f"tr_status={h['translation_status']}\n")
                for w in h["windows"]:
                    f.write(f"  ... {w} ...\n")
                f.write(f"  TR: {h['translation'][:400]}\n")
    print("forms:", len(FORMS))
    for form in FORMS:
        hits = result[form]
        print(f"{form}: {len(hits)} inscriptions, {sum(h['occurrences'] for h in hits)} occurrences")


if __name__ == "__main__":
    main()
