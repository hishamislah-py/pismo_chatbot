"""Score the reasoning-effort experiment (both parts) with deterministic criteria and list paired regressions for manual
review. No model judge. Usage: python -B -E -s analyze_effort.py <bench_answers.jsonl> <e2e.json|-> <out.json>"""
import json
import os
import re
import statistics as st
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(os.path.dirname(HERE))
URL = re.compile(r"https?://[^\s`'\")\]>]+")
BROAD = ("RW-T01", "RW-T02", "RW-T03", "RW-T05", "RW-T06", "RW2-01", "RW2-02", "D2")
FACTS = {"JWT": r"\bJWTs?\b|JSON Web Token", "Authorization header": r"Authorization`? header", "kid": r"\bkid\b",
         "public-keys endpoint": r"/v1/certs", "signature verification": r"verif\w* (the |its )?(JWT |token )?signature",
         "body-hash / SHA256": r"body-hash|SHA-?256"}


def pct(xs, p):
    xs = sorted(x for x in xs if x is not None)
    return xs[min(len(xs) - 1, int(p * len(xs)))] if xs else None


def warn_kind(w):
    return ("unsupported_api_detail" if "not found in the passages" in w else "uncited_api_detail" if "no citation" in w
            else "unmarked_historical" if "historical" in w else "unknown_label" if "not supplied" in w
            else "integration" if "another integration" in w else "no_inline_citations" if "no inline" in w else "other")


def main(argv):
    texts = {}
    for l in open(os.path.join(EXP, "results", "chunks.jsonl"), encoding="utf-8"):
        c = json.loads(l)
        texts[c["chunk_id"]] = c["text"]
    rows = [json.loads(l) for l in open(argv[0], encoding="utf-8")]
    scored = []
    for r in rows:
        ans = r.get("answer") or ""
        ev_text = "\n".join(texts.get(c, "") for _, c in r["evidence"])
        ids = [x["id"] for x in r["refs"]]
        rel = {c for x in r["refs"] for c in x["relevant_chunks"]}
        labelled = any(x["evidence_label_recall"] is not None for x in r["refs"])
        answerability = next((x["answerability"] for x in r["refs"] if x["answerability"]), None)
        urls = [u.rstrip(".,;:") for u in URL.findall(ans)]
        scored.append({
            "arm": r["arm"], "question": r["question"], "ids": ids, "status": r["status"], "valid": r["citations_valid"],
            "warnings": [warn_kind(w) for w in r.get("warnings") or []], "error": r.get("error"),
            "gen_ms": (r.get("call") or {}).get("ms"), "pipeline_ms": r["pipeline_ms"],
            "completion_tokens": (r.get("call") or {}).get("completion_tokens"), "reasoning_tokens": (r.get("call") or {}).get("reasoning_tokens"),
            "words": len(ans.split()), "answerability": answerability, "labelled": labelled,
            "cites_relevant": bool(set(r["citations"]) & rel) if labelled and rel else None,
            "full_evidence": any(x["evidence_label_recall"] == 1.0 for x in r["refs"]),
            "urls_not_in_evidence": [u for u in urls if u not in ev_text],
            "facts": {k: bool(re.search(v, ans, re.I)) for k, v in FACTS.items()} if any(i in BROAD for i in ids) else None,
            "answer": ans})
    out = {"bench": {}, "pairs": {}, "e2e": None}
    for arm in ("default", "low"):
        xs = [x for x in scored if x["arm"] == arm]
        lab = [x for x in xs if x["cites_relevant"] is not None and x["answerability"] != "none"]
        none = [x for x in xs if x["answerability"] == "none"]
        broad = [x for x in xs if x["facts"]]
        out["bench"][arm] = {
            "n": len(xs), "errors": sum(1 for x in xs if x["error"]),
            "gen_ms_median": st.median(x["gen_ms"] for x in xs if x["gen_ms"]), "gen_ms_p90": pct([x["gen_ms"] for x in xs], .9),
            "pipeline_ms_median": st.median(x["pipeline_ms"] for x in xs), "pipeline_ms_p90": pct([x["pipeline_ms"] for x in xs], .9),
            "reasoning_tokens_median": st.median(x["reasoning_tokens"] for x in xs if x["reasoning_tokens"] is not None),
            "completion_tokens_median": st.median(x["completion_tokens"] for x in xs if x["completion_tokens"] is not None),
            "words_median": st.median(x["words"] for x in xs),
            "status": dict(Counter(x["status"] for x in xs)),
            "validator_pass": sum(1 for x in xs if x["valid"]), "validator_rate": round(sum(1 for x in xs if x["valid"]) / len(xs), 3),
            "warning_kinds": dict(Counter(w for x in xs for w in x["warnings"])),
            "cites_relevant": f"{sum(x['cites_relevant'] for x in lab)}/{len(lab)}",
            "false_abstentions": sum(1 for x in xs if x["full_evidence"] and x["status"] == "not_documented"),
            "unanswerable_escalated": f"{sum(1 for x in none if x['status'] in ('not_documented', 'partial'))}/{len(none)}",
            "answers_with_url_not_in_evidence": sum(1 for x in xs if x["urls_not_in_evidence"]),
            "broad_fact_coverage": {k: round(sum(x["facts"][k] for x in broad) / len(broad), 2) for k in FACTS} if broad else None}
    by_q = defaultdict(dict)
    for x in scored:
        by_q[x["question"]][x["arm"]] = x
    worse, better = [], []
    for q, d in by_q.items():
        if len(d) < 2:
            continue
        dflt, low = d["default"], d["low"]
        reasons = []
        if dflt["valid"] and not low["valid"]:
            reasons.append(f"validator fails ({low['warnings']})")
        if dflt["cites_relevant"] and low["cites_relevant"] is False:
            reasons.append("no longer cites labelled evidence")
        if low["full_evidence"] and low["status"] == "not_documented" and dflt["status"] != "not_documented":
            reasons.append("abstains despite full evidence")
        if low["answerability"] == "none" and low["status"] not in ("not_documented", "partial") and dflt["status"] in ("not_documented", "partial"):
            reasons.append("answers an unanswerable question")
        if low["urls_not_in_evidence"] and not dflt["urls_not_in_evidence"]:
            reasons.append(f"URL not in evidence {low['urls_not_in_evidence']}")
        if reasons:
            worse.append({"question": q, "ids": low["ids"], "reasons": reasons, "default_status": dflt["status"], "low_status": low["status"]})
        if low["valid"] and not dflt["valid"]:
            better.append({"question": q, "ids": low["ids"], "default_warnings": dflt["warnings"]})
    out["pairs"] = {"questions": len(by_q), "low_worse": worse, "low_better_validator": better}
    if argv[1] != "-":
        e = json.load(open(argv[1], encoding="utf-8"))["rows"]
        ans = [r for r in e if (r["timings"] or {}).get("llm_ms")]
        out["e2e"] = {}
        for arm in ("default", "low"):
            xs = [r for r in ans if r["arm"] == arm]
            out["e2e"][arm] = {"n_answers": len(xs), "n_requests": sum(1 for r in e if r["arm"] == arm),
                               "http_errors": sum(1 for r in e if r["arm"] == arm and r["http"] != 201),
                               "e2e_ms_median": st.median(r["e2e_ms"] for r in xs), "e2e_ms_p90": pct([r["e2e_ms"] for r in xs], .9),
                               "llm_ms_median": st.median(r["timings"]["llm_ms"] for r in xs), "llm_ms_p90": pct([r["timings"]["llm_ms"] for r in xs], .9),
                               "routing_ms_median": st.median(r["timings"].get("routing_ms") or 0 for r in xs),
                               "validator_rate": round(sum(1 for r in xs if r["citations_valid"]) / len(xs), 3),
                               "status": dict(Counter(r["status"] for r in xs)),
                               "reasoning_tokens_median": st.median((r["call"] or {}).get("reasoning_tokens") or 0 for r in xs)}
    json.dump({"summary": out, "scored": scored}, open(argv[2], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps(out, indent=1, ensure_ascii=False)[:12000])


if __name__ == "__main__":
    main(sys.argv[1:])
