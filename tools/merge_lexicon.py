#!/usr/bin/env python3
"""Merge the Rilly 2003 Vol. II OCR lexicon into the 774-entry lexicon.

Rules, in order:
1. Never upgrade a gloss status. Rilly entries are proposed or rejected only.
2. Never invent a gloss, a form, or a loan status.
3. Dedup key is form_norm, lowercased and stripped. Same form, different
   claim (for example two senses) stays as two records, flagged in the report.
4. When a form already exists:
   - Certain old entry wins. Keep its gloss and status. Merge attestations
     (union). Note the Rilly gloss and page in notes when it differs.
   - Proposed old entry wins as the base record. Merge attestations. Note
     the Rilly gloss, biblio and page in notes when they differ.
   - A status conflict (old rejected vs new proposed, or old certain/proposed
     vs new rejected) keeps the old record and is listed in the report.
     A new rejected entry for a form that stays proposed or certain is added
     as a second record, so the rejection is not lost.
5. New forms are added with their Rilly gloss, pos as printed, attestations,
   biblio, discussion, pdf_page, section, and source_tag
   rilly-2003-vol2-lexicon. is_egyptian_loan is set False only because the
   matcher reads it for certain entries, and no Rilly entry is certain;
   loan status for Rilly entries is unassessed, not "not a loan".
6. Nothing in the old lexicon is deleted or rewritten except merged
   attestations and appended notes.

Inputs:
  source-meroe-philology/public/data/corpus/lexicon.json (774)
  rilly-lexicon-build/rilly-2003-lexicon-v0.1.json (744)
Outputs, in merge-benchmark/:
  lexicon-merged-v0.2.json, merge-report.md
"""
import json
from collections import Counter
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
OLD_PATH = RUN / "source-meroe-philology" / "public" / "data" / "corpus" / "lexicon.json"
NEW_PATH = RUN / "rilly-lexicon-build" / "rilly-2003-lexicon-v0.1.json"
OUT_DIR = RUN / "merge-benchmark"
OUT_DIR.mkdir(exist_ok=True)


def key(form_norm):
    return (form_norm or "").strip().lower()


def merge_atts(old_atts, new_atts):
    out = list(old_atts or [])
    for a in new_atts or []:
        if a not in out:
            out.append(a)
    return out


def main():
    old = json.load(open(OLD_PATH))
    new_raw = json.load(open(NEW_PATH))
    new = new_raw["records"] if isinstance(new_raw, dict) else new_raw

    merged = [dict(e) for e in old]
    by_key = {}
    for i, e in enumerate(merged):
        by_key.setdefault(key(e.get("form_norm")), []).append(i)

    report = {
        "old_total": len(old),
        "new_total": len(new),
        "added_new_forms": 0,
        "merged_into_existing": 0,
        "added_second_record_rejected": 0,
        "status_conflicts": [],
        "duplicate_forms_in_new": [],
        "notes": [],
    }

    new_key_counts = Counter(key(r.get("form_norm")) for r in new)
    for k, v in new_key_counts.items():
        if v > 1:
            report["duplicate_forms_in_new"].append({"form_norm": k, "records": v})

    for r in new:
        k = key(r.get("form_norm"))
        gloss = (r.get("gloss") or "").strip()
        status = r.get("gloss_status") or "proposed"
        existing = by_key.get(k, [])
        if not existing:
            entry = {
                "form": r.get("form"),
                "form_norm": r.get("form_norm"),
                "gloss": gloss,
                "gloss_en": r.get("gloss_en") or "",
                "gloss_status": status,
                "pos": r.get("pos") or "",
                "benchmark_category": "",
                "is_egyptian_loan": False,
                "attestations": list(r.get("attestations") or []),
                "variants": list(r.get("variants") or []),
                "biblio": r.get("biblio") or "",
                "discussion": r.get("discussion") or "",
                "pdf_page": r.get("pdf_page"),
                "section": r.get("section") or "",
                "source": r.get("source") or "Rilly 2003 Vol. II",
                "source_tag": "rilly-2003-vol2-lexicon",
                "permission_status": "academic-fair-use-excerpt",
                "provenance_flag": "rilly-2003-ocr-v0.1",
                "notes": "",
            }
            merged.append(entry)
            by_key.setdefault(k, []).append(len(merged) - 1)
            report["added_new_forms"] += 1
            continue

        base = merged[existing[0]]
        old_status = base.get("gloss_status")
        if status == "rejected" and old_status in ("certain", "proposed"):
            # Keep the old record and add the rejection as a second record,
            # so the conflicting claim is visible, not silently dropped.
            entry = {
                "form": r.get("form"),
                "form_norm": r.get("form_norm"),
                "gloss": gloss,
                "gloss_en": r.get("gloss_en") or "",
                "gloss_status": "rejected",
                "pos": r.get("pos") or "",
                "benchmark_category": "",
                "is_egyptian_loan": False,
                "attestations": list(r.get("attestations") or []),
                "variants": list(r.get("variants") or []),
                "biblio": r.get("biblio") or "",
                "discussion": r.get("discussion") or "",
                "pdf_page": r.get("pdf_page"),
                "section": r.get("section") or "",
                "source": r.get("source") or "Rilly 2003 Vol. II",
                "source_tag": "rilly-2003-vol2-lexicon",
                "permission_status": "academic-fair-use-excerpt",
                "provenance_flag": "rilly-2003-ocr-v0.1",
                "notes": (f"Rilly 2003 rejected section lists this form; "
                          f"kept alongside the existing {old_status} entry."),
            }
            merged.append(entry)
            by_key[k].append(len(merged) - 1)
            report["added_second_record_rejected"] += 1
            report["status_conflicts"].append({
                "form_norm": k, "old_status": old_status,
                "new_status": "rejected", "action": "kept old, added rejected record",
                "pdf_page": r.get("pdf_page")})
            continue
        if status == "proposed" and old_status == "rejected":
            report["status_conflicts"].append({
                "form_norm": k, "old_status": "rejected",
                "new_status": "proposed", "action": "kept rejected, no change",
                "pdf_page": r.get("pdf_page")})
            continue

        # Same status family: merge attestations, note a differing gloss.
        before = len(base.get("attestations") or [])
        base["attestations"] = merge_atts(base.get("attestations"), r.get("attestations"))
        added_atts = len(base["attestations"]) - before
        note = base.get("notes") or ""
        if gloss and gloss != (base.get("gloss") or ""):
            add = f"Rilly 2003 (p. {r.get('pdf_page')}): {gloss}."
            if add not in note:
                note = (note + " " + add).strip()
        if r.get("biblio"):
            add = f"Rilly 2003 biblio (p. {r.get('pdf_page')}): {r.get('biblio')}"
            if add not in note:
                note = (note + " " + add).strip()
        base["notes"] = note
        base["source_tag"] = (base.get("source_tag") or "") + "+rilly-2003-vol2-lexicon"
        report["merged_into_existing"] += 1
        if added_atts:
            report["notes"].append(f"{k}: +{added_atts} attestations from Rilly 2003")

    out = {
        "version": "0.2.0-merged",
        "source": "lexicon.json (774) + rilly-2003-lexicon-v0.1.json (744)",
        "counts": dict(Counter(e.get("gloss_status") for e in merged)),
        "records": merged,
    }
    json.dump(out, open(OUT_DIR / "lexicon-merged-v0.2.json", "w"),
              indent=2, ensure_ascii=False)
    report["merged_total"] = len(merged)
    report["merged_by_status"] = dict(Counter(e.get("gloss_status") for e in merged))
    distinct = len({key(e.get("form_norm")) for e in merged})
    report["distinct_form_norms"] = distinct
    json.dump(report, open(OUT_DIR / "merge-report.json", "w"), indent=2, ensure_ascii=False)
    print(json.dumps({k: v for k, v in report.items() if k != "notes"}, indent=2))
    print("WROTE lexicon-merged-v0.2.json merge-report.json")


if __name__ == "__main__":
    main()
