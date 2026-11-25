#!/usr/bin/env python3
"""Build u3-retest.json from the extractor output and the judged verdicts.

Verdicts were judged by hand against the attestations in attestations.txt,
following the U3 method in u3-contextual-tests-v3.md: a candidate needs at
least 3 decided inscriptions; the two REM 0094 witnesses count as one
inscription; a meaning is supported only when it fits across multiple
independent inscriptions. No gloss is upgraded. Read-only outside this folder.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]

ranked = json.load(open(HERE / "_newly_covered_ranked.json"))["ranked"]
atts = json.load(open(HERE / "attestations.json"))
lex = json.load(open(RUN / "merge-benchmark" / "lexicon-merged-v0.2.json"))["records"]

import re

def clean(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

# Rebuild the matcher maps exactly as recompute_merged.py does.
certain_forms = {}
proposed_forms = {}
for e in lex:
    k = clean(e.get("form_norm"))
    if not k:
        continue
    if e.get("gloss_status") == "certain":
        certain_forms[k] = e
    elif e.get("gloss_status") == "proposed":
        proposed_forms[k] = e

def match_token(raw):
    c = clean(raw)
    if c in certain_forms:
        return ("certain", certain_forms[c], "exact")
    if c in proposed_forms:
        return ("proposed", proposed_forms[c], "exact")
    for stem, entry in certain_forms.items():
        if len(stem) >= 3 and (c.startswith(stem) or (len(stem) >= 4 and stem in c)):
            return ("certain", entry, "stem")
    for stem, entry in proposed_forms.items():
        if len(stem) >= 4 and c.startswith(stem):
            return ("proposed", entry, "stem")
    return (None, None, None)

# form -> (verdict, support, refutation, uninformative, evidence_for, evidence_against, notes)
# Attestation lists below are inscription IDs from attestations.json.
V = {
 "mtr": ("untested", ["OTTEN-MILLET-0104"], [],
         ["REM 0094", "OTTEN-MILLET-0255", "OTTEN-MILLET-0256", "OTTEN-MILLET-0261"],
         "The 0104 translation renders the passage as directions, cush-wards to Adere and northwards to Philae, and mtr stands after each place name in that list.",
         "None.",
         "All five inscriptions quote one REM 0094 passage, so the support counts once. The bar is 3 decided inscriptions."),
 "wse": ("untested", ["REM 0094"], [],
         ["REM 1044", "REM 1003"],
         "Millet renders 'mte ws' as 'the mte of the land', which puts land in the wse slot.",
         "None.",
         "One support only. The other two inscriptions give no translation that covers wse."),
 "yed": ("untested", ["OTTEN-MILLET-0145"], [],
         ["REM 0094", "REM 0081", "OTTEN-MILLET-0336"],
         "The 0145 translation lists '1 bXe of the yed' and '16 yed tlt he donated' among donated goods, so yed is a counted commodity.",
         "None.",
         "One support only. 0336 quotes the same passage as 0145 without a translation."),
 "wido": ("untested", [], [],
          ["REM 1044", "REM 1003", "REM 0094"],
          "None independent.",
          "None.",
          "The only published rendering of wido as 'that is to say' (Millet on REM 0094/25, cited in Rilly) is the source of the gloss itself, so it cannot count as independent support."),
 "aro": ("untested", [], [],
         ["REM 1044", "REM 1003"],
         "None.",
         "None.",
         "The gloss field mixes three rival readings: Priese 'im Himmel', Cottevieille-Giraudet and Zyhlarz 'roi' (rejected by Priese), Abdalla 'Horus'. 'Roi' was tested here. 'Aro bel' repeats as a formula in REM 1003 and no translation covers aro."),
 "meke": ("untested", [], [],
          ["REM 1044", "REM 1003"],
          "None.",
          "None.",
          "The phrase 'seb meke adb' repeats in REM 1003 and no translation covers meke in any inscription."),
 "penn": ("supported",
          ["OTTEN-MILLET-0055", "OTTEN-MILLET-0150", "REM 0089",
           "OTTEN-MILLET-0341", "OTTEN-MILLET-0353", "OTTEN-MILLET-0354"],
          [],
          ["REM 0094", "OTTEN-MILLET-0254", "OTTEN-MILLET-0352"],
          "0150 reads 'fifth year of the penn-cycle', 0089 reads 'penn 30+4', and 0353 reads 'penn 5ni'. Penn takes ordinals and numbers like a year word.",
          "None.",
          "Support is the U3-11 result, reused here: the Rilly gloss 'annee' is the same year sense U3-11 tested. The merge added only REM 0094 tokens, already uninformative in U3-11 ('plw penn tlte'). The second Rilly sense, 'lever (d'un astre)', has no context anywhere and stays untested."),
 "nte": ("untested", [], [],
         ["REM 1044", "OTTEN-MILLET-0154", "OTTEN-MILLET-0342", "OTTEN-MILLET-0344"],
         "None.",
         "None.",
         "The 0154 translation leaves 'nte-yd.eSxini' unrendered. 0342 and 0344 quote the same passage without a translation."),
 "sor": ("untested", [], [],
         ["REM 1044", "REM 0089"],
         "None.",
         "None.",
         "No translation covers sor in either inscription."),
 "aleqese": ("untested", [], [],
            ["REM 1044", "REM 1003", "REM 0075"],
            "None.",
            "None.",
            "The inscription-initial slot fits invocation and monument equally, and Rilly allows 'substantif ou pronom', so position does not decide."),
 "qoro": ("untested", [], [],
          ["REM 1044", "REM 0003", "REM 0069", "REM 0073", "REM 0089"],
          "None.",
          "None.",
          "No translation covers qoro. Rilly's own case for 'c'est le souverain' rests on a parallel in REM 1294, which is unpublished and not in this corpus."),
 "sedew": ("untested", [], [],
           ["REM 1044"],
           "None.",
           "None.",
           "Only one inscription holds sedew."),
 "tre": ("untested", [], ["OTTEN-MILLET-0001"],
         ["REM 0094 (Millet Witness)"],
         "None.",
         "0001 renders 'qEre tre' as 'Tarenas, kdwe-lady', so tre sits inside a personal name and cannot be the verb give there.",
         "One refutation only. The REM 0094 witness gives no translation for 'trE s ariteN'."),
 "yeyk": ("untested", [], [],
          ["REM 0094"],
          "None.",
          "None.",
          "Both witnesses of REM 0094 count as one inscription, and no translation covers yeyk."),
 "ntk": ("untested", [], [],
         ["REM 1044"],
         "None.",
         "None.",
         "Only one inscription holds ntk, and one occurrence is the broken token 'nt[.]k'."),
 "pyk": ("untested", [], [],
         ["REM 0094"],
         "None.",
         "None.",
         "Both witnesses of REM 0094 count as one inscription, and no translation covers pyk."),
 "bqo": ("untested", [], [],
         ["REM 0094"],
         "None.",
         "None.",
         "Only one inscription holds bqo."),
 "nete": ("untested", [], [],
          ["REM 1003"],
          "None.",
          "None.",
          "Only one inscription holds nete, in 'amnp nete se', and no translation covers it."),
 "netese": ("untested", [], [],
            ["REM 1044"],
            "None.",
            "None.",
            "Stem match to nete 'pere'. Only one inscription holds netese, and the gloss belongs to the stem, not to this form."),
 "sete": ("untested", [], [],
          ["REM 1044"],
          "None.",
          "None.",
          "Only one inscription holds sete. Rilly notes the father reading is contradicted ('unwahrscheinlich') and Millet suggests 'nephew'."),
 "terite": ("untested", [], [],
            ["REM 1044"],
            "None.",
            "None.",
            "Only one inscription holds terite, in the opening line 'lw terite amnpte', and no translation covers it."),
 "wete": ("untested", [], [],
          ["REM 1003"],
          "None.",
          "None.",
          "Only one inscription holds wete."),
 "yemoqe": ("untested", [], [],
            ["REM 1003"],
            "None.",
            "None.",
            "Only one inscription holds yemoqe."),
 "yeyki": ("untested", [], [],
           ["REM 0094 (Millet Witness)"],
           "None.",
           "None.",
           "Stem match to yeyk 'chacun'. Only one inscription holds yeyki."),
 "yetolxe": ("untested", [], [],
             ["REM 0094"],
             "None.",
             "None.",
             "Stem match to yeto 'eau'. Only one inscription holds yetolxe."),
 "mrorbe": ("untested", [], [],
            ["REM 0094"],
            "None.",
            "None.",
            "Stem match to mror 'young one'. Only one inscription holds mrorbe."),
 "mrorleb": ("untested", [], [],
             ["REM 0094"],
             "None.",
             "None.",
             "Stem match to mror 'young one'. Only one inscription holds mrorleb."),
 "adenodorte": ("untested", [], [],
                ["REM 1044"],
                "None.",
                "None.",
                "Stem match to adenodor 'Dendour'. Only one inscription holds adenodorte."),
 "bto": ("untested", [], [],
         ["REM 1044"],
         "None.",
         "None.",
         "The gloss 'established before Isis' is a phrase gloss for a suffix in 'Wos-se-bto' at Philae. The one corpus occurrence is 'eked bto krte' in REM 1044, and no translation covers it."),
 "amnp": ("untested", [], [],
          ["REM 1044", "REM 1003"],
          "None.",
          "None.",
          "No candidate meaning: the merged entry for amnp has no gloss, only the part of speech 'nom de'."),
 "dete": ("untested", [], [],
          ["REM 1003", "REM 0094", "OTTEN-MILLET-0255", "OTTEN-MILLET-0256"],
          "None.",
          "None.",
          "No candidate meaning: the merged entry for dete has no gloss."),
 "kek": ("untested", [], [],
         ["REM 1044", "REM 0075"],
         "None.",
         "None.",
         "No candidate meaning: the merged entry for kek has no gloss."),
 "kete": ("untested", [], [],
          ["REM 1044"],
          "None.",
          "None.",
          "No candidate meaning: the merged entry '-kete' has no gloss."),
 "tepke": ("untested", [], [],
           ["REM 1044", "REM 0094"],
           "None.",
           "None.",
           "No candidate meaning: the merged entry for tepke has no gloss."),
 "tmot": ("untested", [], [],
          ["REM 1044", "REM 1003", "REM 0094"],
          "None.",
          "None.",
          "No candidate meaning: the merged entry for tmot has no gloss."),
 "wit": ("untested", [], [],
         ["REM 1044", "REM 1003"],
         "None.",
         "None.",
         "No candidate meaning: the merged entry for wit has no gloss."),
 "lks": ("untested", [], [],
         ["REM 1044", "REM 1003", "REM 0094", "OTTEN-MILLET-0255"],
         "None.",
         "None.",
         "No candidate meaning: the merged entry for lks has no gloss."),
 "mnitke": ("untested", [], [],
            ["REM 0094", "OTTEN-MILLET-0255"],
            "None.",
            "None.",
            "No candidate meaning: the merged entry for mnitke has no gloss."),
 "mse": ("untested", [], [],
         ["REM 1044", "REM 1003"],
         "None.",
         "None.",
         "No candidate meaning: the merged entry for mse has no gloss."),
 "eqe": ("untested", [], [],
         ["REM 1003"],
         "None.",
         "None.",
         "No clean candidate meaning: the gloss field is garbled discussion text, and Rilly states the sense remains uncertain, with 'preterit' only hypothetical."),
 "simlok": ("untested", [], [],
            ["REM 0094"],
            "None.",
            "None.",
            "No clean candidate meaning: simlok is a stem match to simlo, whose gloss 'de Simloa Selele' is a toponym fragment, not a meaning for simlok."),
}

out = {"title": "U3 retest: Rilly-merge newly covered forms",
       "method": "U3 contextual hypothesis testing (u3-contextual-tests-v3.md). "
                 "A candidate needs at least 3 decided inscriptions. "
                 "The two REM 0094 witnesses count as one inscription. "
                 "No gloss is upgraded.",
       "verification": {
           "newly_covered_tokens_total": 178,
           "newly_covered_by_narrative": {"REM 1044": 65, "REM 1003": 41,
                                           "REM 0094 (FHN)": 45, "REM 0094 (Millet)": 27},
           "arithmetic": "Old gap tokens 1535 minus new gap tokens 1357 equals 178. "
                         "Per narrative: 505-440=65, 326-285=41, 159-114=45, 545-518=27. "
                         "The gap-list diff gives the same four numbers and 73 distinct forms.",
           "gap_tokens_old": 1535, "gap_tokens_new": 1357,
           "gap_types_old": 715, "gap_types_new": 642,
           "newly_covered_distinct_forms": 73,
           "spot_checks": [
               "mtr: OTTEN-MILLET-0104 translation reads 'cush-wards to adere ..... northwards to philae .....', and its transcription is 'qeSw : adereke : mtr : ws : Xrw : pilqeke : mtr : ws :'.",
               "yed: OTTEN-MILLET-0145 translation lists '1 bXe of the yed' and '16 yed tlt he donated' among donated goods.",
               "penn: u3-tests-v3.json U3-11 records support 6 with inscriptions OTTEN-MILLET-0055, OTTEN-MILLET-0150, REM 0089, OTTEN-MILLET-0341, OTTEN-MILLET-0353, OTTEN-MILLET-0354, verdict supported."
           ]},
       "summary": {},
       "tested": []}

NO_CANDIDATE = {"amnp", "dete", "kek", "kete", "tepke", "tmot", "wit",
                "lks", "mnitke", "mse", "eqe", "simlok"}

n_sup = n_ref = n_unt = 0
judged_forms = [e for e in ranked if e["form"] in V]
remaining = [e["form"] for e in ranked if e["form"] not in V]
for e in judged_forms:
    f = e["form"]
    st, entry, mode = match_token(f)
    hits = atts.get(f, [])
    checked = sorted({h["id"] for h in hits})
    if f in V:
        verdict, sup, ref, uninf, ev_for, ev_against, notes = V[f]
        if f in NO_CANDIDATE:
            # No candidate meaning: every checked inscription is uninformative.
            uninf = checked
    else:
        verdict, sup, ref, uninf, ev_for, ev_against, notes = (
            "untested", [], [], checked, "None.", "None.", "Not judged.")
    if verdict == "supported":
        n_sup += 1
    elif verdict == "refuted":
        n_ref += 1
    else:
        n_unt += 1
    out["tested"].append({
        "form": f,
        "new_tokens": e["new_tokens"],
        "new_tokens_by_narrative": e["by_narrative"],
        "matched_entry": {
            "form_norm": entry.get("form_norm") if entry else None,
            "gloss": entry.get("gloss") if entry else None,
            "gloss_status": entry.get("gloss_status") if entry else None,
            "pos": entry.get("pos") if entry else None,
            "source": entry.get("source") if entry else None,
            "pdf_page": entry.get("pdf_page") if entry else None,
            "match_mode": mode,
        } if entry else None,
        "candidate_meaning": (entry.get("gloss") if entry and entry.get("gloss") else None),
        "attestations_checked": checked,
        "attestation_inscription_count": len(checked),
        "support_count": len(sup),
        "support_inscriptions": sup,
        "refutation_count": len(ref),
        "refutation_inscriptions": ref,
        "uninformative_count": len(uninf),
        "uninformative_inscriptions": uninf,
        "verdict": verdict,
        "evidence_for": ev_for,
        "evidence_against": ev_against,
        "notes": notes,
    })

out["summary"] = {
    "forms_recorded": len(out["tested"]),
    "forms_tested_with_candidate_gloss": 29,
    "forms_with_no_candidate_meaning": 12,
    "supported": n_sup,
    "refuted": n_ref,
    "untested": n_unt,
    "top_20_forms_tested": 20,
    "extra_forms_tested": len(out["tested"]) - 20,
    "newly_covered_forms_total": 73,
    "remaining_unjudged_forms": len(remaining),
    "remaining_unjudged_form_list": remaining,
}
json.dump(out, open(HERE / "u3-retest.json", "w"), indent=1, ensure_ascii=False)
print("forms:", len(out["tested"]), "supported:", n_sup, "refuted:", n_ref, "untested:", n_unt)
print("no-candidate forms:", [t["form"] for t in out["tested"] if not t["candidate_meaning"]])
