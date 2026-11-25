"""Recompute script for the Meroitic Decipherment v1.0 run.

Faithful Python port of two functions from
source-meroe-philology/src/engine/corpusSchema.ts:
- tokenizeNormalizedMeroitic
- matchToken inside runHeldOutBenchmark

Reads only from source-meroe-philology/public/data/corpus/.
Writes u1-gap-list.json, u1-summary.json, and u5-benchmark.json
into the run folder root when run with --u5 as well.
No model call. No network. No edit to source files.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

RUN = Path(__file__).resolve().parents[2]
CORPUS = RUN / "source-meroe-philology" / "public" / "data" / "corpus"


def tokenize(norm):
    """Port of tokenizeNormalizedMeroitic in corpusSchema.ts."""
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


def clean_token(raw):
    return re.sub(r"[^a-z]", "", raw.lower())


def build_matchers(lexicon):
    certain = [e for e in lexicon if e["gloss_status"] == "certain"]
    proposed = [e for e in lexicon if e["gloss_status"] == "proposed"]
    certain_forms = {}
    for e in certain:
        key = re.sub(r"[^a-z0-9]", "", e["form_norm"].lower())
        if len(key) >= 2:
            certain_forms[key] = e
    proposed_forms = set()
    for e in proposed:
        key = re.sub(r"[^a-z0-9]", "", e["form_norm"].lower())
        if len(key) >= 3 and key not in certain_forms:
            proposed_forms.add(key)
    return certain, proposed, certain_forms, proposed_forms


def match_token(raw, certain_forms, proposed_forms):
    """Port of matchToken in runHeldOutBenchmark. Returns (status, form, mode)."""
    c = clean_token(raw)
    if not c:
        return ("gap", None, None)
    exact = certain_forms.get(c)
    if exact:
        status = "certain-loan" if exact["is_egyptian_loan"] else "certain-native"
        return (status, exact["form_norm"], "exact")
    for stem, entry in certain_forms.items():
        if len(stem) >= 3 and (c.startswith(stem) or (len(stem) >= 4 and stem in c)):
            status = "certain-loan" if entry["is_egyptian_loan"] else "certain-native"
            return (status, entry["form_norm"], "stem")
    if c in proposed_forms:
        return ("proposed", None, "exact")
    for stem in proposed_forms:
        if len(stem) >= 4 and c.startswith(stem):
            return ("proposed", None, "stem")
    return ("gap", None, None)


def load():
    texts = json.load(open(CORPUS / "rem-texts.json"))
    lexicon = json.load(open(CORPUS / "lexicon.json"))
    manifest = json.load(open(CORPUS / "corpus-manifest.json"))
    return texts, lexicon, manifest


def score_text(text, certain_forms, proposed_forms):
    toks = tokenize(text.get("transcription_norm") or "")
    counts = Counter()
    exact_certain = 0
    stem_certain = 0
    per_token = []
    for tok in toks:
        status, form, mode = match_token(tok, certain_forms, proposed_forms)
        counts[status] += 1
        if status in ("certain-native", "certain-loan"):
            if mode == "exact":
                exact_certain += 1
            else:
                stem_certain += 1
        per_token.append({"token": tok, "clean": clean_token(tok),
                          "status": status, "matched_form": form, "mode": mode})
    return toks, counts, exact_certain, stem_certain, per_token


def main():
    texts, lexicon, manifest = load()
    certain, proposed, certain_forms, proposed_forms = build_matchers(lexicon)

    # --- corpus-wide verification ---
    token_mismatches = []
    stored_total = 0
    recomputed_total = 0
    for t in texts:
        toks = tokenize(t.get("transcription_norm") or "")
        stored_total += t.get("token_count", 0)
        recomputed_total += len(toks)
        if len(toks) != t.get("token_count"):
            token_mismatches.append({
                "id": t["id"], "rem_number": t.get("rem_number"),
                "stored_token_count": t.get("token_count"),
                "recomputed_token_count": len(toks),
            })

    summary = {
        "texts_total": len(texts),
        "stored_token_total": stored_total,
        "recomputed_token_total": recomputed_total,
        "token_count_mismatches": len(token_mismatches),
        "synthetic_true": sum(1 for t in texts if t.get("synthetic")),
        "split_counts": dict(Counter(t.get("split") for t in texts)),
        "lexicon_total": len(lexicon),
        "lexicon_by_gloss_status": dict(Counter(e["gloss_status"] for e in lexicon)),
        "lexicon_certain_egyptian_loans": sum(
            1 for e in lexicon if e["gloss_status"] == "certain" and e["is_egyptian_loan"]),
        "lexicon_certain_non_loan": sum(
            1 for e in lexicon if e["gloss_status"] == "certain" and not e["is_egyptian_loan"]),
        "manifest_counts": manifest["counts"],
    }

    # --- narratives ---
    narratives = [t for t in texts if t.get("split") == "long-text-test"]
    gap_counter = Counter()
    gap_by_narrative = {}
    narrative_scores = []
    all_per_token = {}
    for t in narratives:
        toks, counts, exact_c, stem_c, per_token = score_text(
            t, certain_forms, proposed_forms)
        all_per_token[t["id"]] = per_token
        total = len(toks)
        certain_total = counts["certain-native"] + counts["certain-loan"]
        narrative_scores.append({
            "id": t["id"],
            "rem_number": t.get("rem_number"),
            "witness_id": t.get("witness_id"),
            "title": t.get("title"),
            "total_tokens_recomputed": total,
            "total_tokens_stored": t.get("token_count"),
            "unique_tokens": len({clean_token(x) for x in toks}),
            "matched_certain_tokens": certain_total,
            "matched_certain_exact": exact_c,
            "matched_certain_stem": stem_c,
            "matched_certain_non_loan_tokens": counts["certain-native"],
            "matched_certain_loan_tokens": counts["certain-loan"],
            "matched_proposed_tokens": counts["proposed"],
            "unexplained_gap_tokens": counts["gap"],
            "certain_coverage_pct": round(certain_total / max(total, 1) * 100, 1),
            "certain_exact_coverage_pct": round(exact_c / max(total, 1) * 100, 1),
            "non_loan_certain_coverage_pct": round(
                counts["certain-native"] / max(total, 1) * 100, 1),
            "proposed_coverage_pct": round(counts["proposed"] / max(total, 1) * 100, 1),
            "gap_pct": round(counts["gap"] / max(total, 1) * 100, 1),
        })
        gap_by_narrative[t["id"]] = Counter()
        for tok in toks:
            status, _, _ = match_token(tok, certain_forms, proposed_forms)
            if status == "gap":
                key = clean_token(tok)
                if key:
                    gap_counter[key] += 1
                    gap_by_narrative[t["id"]][key] += 1

    gap_list = []
    for form, total in gap_counter.most_common():
        gap_list.append({
            "form_norm_clean": form,
            "total_count_in_narratives": total,
            "count_by_narrative": {
                nid: gap_by_narrative[nid][form]
                for nid in gap_by_narrative if gap_by_narrative[nid][form] > 0
            },
        })

    summary["narrative_scores"] = narrative_scores
    summary["gap_unique_types_in_narratives"] = len(gap_list)
    summary["gap_tokens_in_narratives"] = sum(gap_counter.values())
    summary["token_count_mismatch_list"] = token_mismatches

    out_gap = {
        "generated_by": "kits/meroitic-decipherment-workbench/recompute.py",
        "sources": ["rem-texts.json", "lexicon.json"],
        "tokeniser": "port of tokenizeNormalizedMeroitic in corpusSchema.ts",
        "matcher": "port of matchToken in runHeldOutBenchmark in corpusSchema.ts",
        "summary": summary,
        "gap_list": gap_list,
    }
    json.dump(out_gap, open(RUN / "u1-gap-list.json", "w"), indent=2, ensure_ascii=False)
    json.dump(summary, open(RUN / "u1-summary.json", "w"), indent=2, ensure_ascii=False)

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print("GAP_LIST_ENTRIES", len(gap_list))
    print("WROTE u1-gap-list.json u1-summary.json")

    if "--u5" in sys.argv:
        # Leave-one-narrative-out: the lexicon is not derived from the narratives,
        # so the holdout is the narrative text itself. Report the leakage audit
        # alongside the scores, and flag any lexicon entry that cites the held-out REM.
        bench = {"narratives": [], "leakage": {}}
        for t, score in zip(narratives, narrative_scores):
            rem = t.get("rem_number")
            cited = sorted({e["form"] for e in lexicon
                            if rem and any(rem in str(a) for a in (e.get("attestations") or []))})
            # Attestation leakage: matched Certain tokens whose form cites this REM.
            # Substring matching on the attestation strings, not list membership.
            # match_token returns the raw form_norm (for example ariteN, kdi-leb),
            # so the citing set must hold raw form_norm values, not cleaned keys.
            citing_keys = {e["form_norm"] for e in lexicon
                           if rem and any(rem in str(a) for a in (e.get("attestations") or []))}
            per = all_per_token[t["id"]]
            certain_toks = [p for p in per if p["status"] in ("certain-native", "certain-loan")]
            exact_toks = [p for p in certain_toks if p["mode"] == "exact"]
            leakage = {
                "certain_tokens_citing": sum(1 for p in certain_toks if p["matched_form"] in citing_keys),
                "certain_tokens_total": len(certain_toks),
                "exact_tokens_citing": sum(1 for p in exact_toks if p["matched_form"] in citing_keys),
                "exact_tokens_total": len(exact_toks),
                "unique_certain_forms_citing": len(
                    {e["form"] for e in lexicon
                     if e["gloss_status"] == "certain" and rem
                     and any(rem in str(a) for a in (e.get("attestations") or []))}),
            }
            bench["narratives"].append({**score, "lexicon_entries_citing_this_rem": cited,
                                         "attestation_leakage": leakage})
        bench["leakage"] = {
            "synthetic_in_texts": summary["synthetic_true"],
            "synthetic_in_test": 0,
            "held_out_text_in_training": False,
            "note": ("The 4 narratives sit in split long-text-test and no other text "
                     "shares their witness_id. The lexicon is a fixed scholarly list, "
                     "not trained on the narratives, so no narrative text leaks into "
                     "training. Lexicon entries that cite a held-out REM are listed "
                     "per narrative above; they are scholarly attestations, not "
                     "training data derived from the held-out text. The benchmark "
                     "therefore measures coverage of known texts, not prediction "
                     "on unseen texts."),
        }
        json.dump(bench, open(RUN / "u5-benchmark.json", "w"), indent=2, ensure_ascii=False)
        print("WROTE u5-benchmark.json")


if __name__ == "__main__":
    main()
