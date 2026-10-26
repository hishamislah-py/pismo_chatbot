"""Score the live answers written by live_compare_versions.py with deterministic, documented criteria (no model judge).

Criteria
- cites_relevant: the answer cites at least one evidence passage that satisfies the question's existing labels.
- cites_unrelated: cited passages that are neither labelled-relevant nor from a labelled KU.
- validator: citations_valid from pismo_assistant.citations (token support, uncited API details, history marking, ...).
- escalation: for answerability "none", correct when status is not_documented or partial; for labelled answerable
  questions whose evidence holds every label, "not_documented" counts as a false abstention.
- contamination: the data-platform production URL (prod.pismo.io) appears in an answer to a client-webhook question.
- body-hash: answers to body-hash questions that present the removed claims-table wording or a conflict.
- webhook fact checklist (NEW criteria written from source lines 20-32, 168-173, 210 and 226-229 of
  docs/get-started/verifying-webhook-requests.md; not part of any benchmark): JWT, Authorization header, kid, public-keys
  endpoint (/v1/certs), signature verification, body-hash/SHA256.

Usage: python -B -E -s scripts/analyze_live_versions.py <retrieval.json> <live_answers.jsonl> <out.json>
"""
import json
import os
import re
import statistics as st
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import common  # noqa: E402

BODY_HASH = ("RW-C01", "RW2-06", "DG07")
BROAD = ("RW-T01", "RW-T02", "RW-T03", "RW-T05", "RW-T06", "RW2-01", "RW2-02", "D2")
FACTS = {"JWT": r"\bJWTs?\b|JSON Web Token", "Authorization header": r"Authorization`? header",
         "kid": r"\bkid\b", "public-keys endpoint": r"/v1/certs", "signature verification": r"verif\w* (the |its )?(JWT |token )?signature",
         "body-hash / SHA256": r"body-hash|SHA-?256"}
REMOVED = "digest of the base64 encoded"
DP_URL = "prod.pismo.io"


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p * len(xs)))] if xs else None


def main(argv):
    ret = json.load(open(argv[0], encoding="utf-8"))
    answers = [json.loads(l) for l in open(argv[1], encoding="utf-8")]
    bench = common.load_json(os.path.join(common.EXP, "BENCHMARK.json"))
    answerability = {q["id"]: q.get("answerability") for q in bench["primary"] + bench["extension"]}
    for f in ("regression_webhook_auth_v1.json", "regression_webhook_auth_v2.json"):
        for q in common.load_json(os.path.join(common.EXP, "benchmark_inputs", f))["questions"]:
            answerability[q["id"]] = q.get("answerability")
    # per version and question text: labelled rows (relevance of each evidence chunk) from the retrieval run
    rows = defaultdict(dict)
    for v, vd in ret["versions"].items():
        for s, rs in vd["questions"].items():
            for r in rs:
                rows[v].setdefault(r["question"], []).append((s, r))

    scored = []
    for a in answers:
        labelled = [(s, r) for s, r in rows[a["version"]][a["question"]] if r["labelled"]]
        ids = [r["id"] for _, r in rows[a["version"]][a["question"]]]
        rel = {e["chunk_id"] for _, r in labelled for e in r["evidence"] if e["relevant"]}
        same_ku = {e["chunk_id"] for _, r in labelled for e in r["evidence"] if e["same_ku_as_label"]}
        cited = [c["chunk_id"] for c in a["citations"]]
        ans = a.get("answer") or ""
        webhook_q = "webhook" in a["question"].lower()
        kinds = Counter()
        for w in a.get("warnings") or []:
            kinds["unsupported_api_detail" if "not found in the passages" in w else "uncited_api_detail" if "no citation" in w
                  else "unmarked_historical" if "historical" in w else "unknown_label" if "not supplied" in w
                  else "no_inline_citations" if "no inline citations" in w else "other"] += 1
        full_ev = any(r.get("evidence_label_recall") == 1.0 for _, r in labelled)
        rec = {"version": a["version"], "question": a["question"], "ids": ids, "repeat": a["repeat"], "status": a["status"],
               "error": a.get("error"), "valid": a.get("citations_valid"), "warning_kinds": dict(kinds),
               "answer_ms": a["answer_ms"], "words": len(ans.split()),
               "tokens": (a.get("call") or {}).get("completion_tokens"),
               "answerability": next((answerability.get(i) for i in ids if answerability.get(i)), None),
               "labelled": bool(labelled), "cites_relevant": bool(set(cited) & rel) if labelled else None,
               "cites_unrelated": sum(1 for c in cited if c not in rel and c not in same_ku) if labelled else None,
               "false_abstention": bool(labelled and full_ev and a["status"] == "not_documented"),
               "dp_url_in_webhook_answer": webhook_q and DP_URL in ans,
               "body_hash_removed_wording": any(i in BODY_HASH for i in ids) and REMOVED in ans.lower(),
               "body_hash_conflict_status": any(i in BODY_HASH for i in ids) and a["status"] == "conflicting_sources",
               "facts": {k: bool(re.search(rx, ans, re.I)) for k, rx in FACTS.items()} if any(i in BROAD for i in ids) else None}
        if rec["answerability"] == "none":
            rec["escalated_correctly"] = a["status"] in ("not_documented", "partial")
        scored.append(rec)

    summary = {}
    for v in ret["versions"]:
        xs = [r for r in scored if r["version"] == v]
        if not xs:
            continue
        lab = [r for r in xs if r["labelled"] and r["answerability"] not in ("none",)]
        none_q = [r for r in xs if r["answerability"] == "none"]
        broad = [r for r in xs if r["facts"]]
        summary[v] = {
            "answers": len(xs), "errors": sum(1 for r in xs if r["error"]),
            "status": dict(Counter(r["status"] for r in xs)),
            "validator_pass_rate": round(sum(1 for r in xs if r["valid"]) / len(xs), 3),
            "warning_kinds": dict(sum((Counter(r["warning_kinds"]) for r in xs), Counter())),
            "labelled_answerable": len(lab),
            "cites_relevant_rate": round(sum(r["cites_relevant"] for r in lab) / len(lab), 3) if lab else None,
            "cites_unrelated_mean": round(st.mean(r["cites_unrelated"] for r in lab), 3) if lab else None,
            "false_abstentions": sum(r["false_abstention"] for r in xs),
            "unanswerable": len(none_q), "escalated_correctly": sum(r["escalated_correctly"] for r in none_q),
            "dp_url_in_webhook_answers": sum(r["dp_url_in_webhook_answer"] for r in xs),
            "body_hash_answers": sum(1 for r in xs if any(i in BODY_HASH for i in r["ids"])),
            "body_hash_removed_wording": sum(r["body_hash_removed_wording"] for r in xs),
            "body_hash_conflict_status": sum(r["body_hash_conflict_status"] for r in xs),
            "broad_webhook_answers": len(broad),
            "broad_fact_coverage": {k: round(sum(r["facts"][k] for r in broad) / len(broad), 2) for k in FACTS} if broad else None,
            "answer_ms_median": st.median(r["answer_ms"] for r in xs), "answer_ms_p90": pct([r["answer_ms"] for r in xs], 0.9),
            "words_median": st.median(r["words"] for r in xs)}
    # variability: same question, evidence identical in all three versions -> three samples of the same input
    by_q = defaultdict(dict)
    ev_by = {(v, q): tuple(e["chunk_id"] for e in rs[0][1]["evidence"]) for v in rows for q, rs in rows[v].items()}
    for r in scored:
        if r["repeat"] == 0:
            by_q[r["question"]][r["version"]] = r
    same = [q for q, d in by_q.items() if len(d) == 3 and len({ev_by[(v, q)] for v in ("v1", "v1.1", "v1.2")}) == 1]
    var = {"questions_with_identical_evidence": len(same),
           "status_agree_all_three": sum(1 for q in same if len({by_q[q][v]["status"] for v in by_q[q]}) == 1),
           "validator_agree_all_three": sum(1 for q in same if len({by_q[q][v]["valid"] for v in by_q[q]}) == 1)}
    reps = defaultdict(list)
    for r in scored:
        reps[(r["version"], r["question"])].append(r)
    rp = [x for x in reps.values() if len(x) > 1]
    var["repeated_pairs"] = len(rp)
    var["repeat_status_agree"] = sum(1 for x in rp if len({r["status"] for r in x}) == 1)
    var["repeat_validator_agree"] = sum(1 for x in rp if len({r["valid"] for r in x}) == 1)
    out = {"criteria": __doc__, "summary": summary, "variability": var, "answers": scored}
    common.dump_json(os.path.abspath(argv[2]), out)
    print(json.dumps({"summary": summary, "variability": var}, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])
