"""Demo-readiness verification: runs both test suites and the six demo questions through the real pipeline, checks
fixed expectations, prints a terminal summary and refreshes the generated section of docs/DEMO_READINESS_VERIFICATION.md.

    python -B -s -m pismo_assistant.verify_demo            # live OpenAI if OPENAI_API_KEY is set in .env, else mocked
    python -B -s -m pismo_assistant.verify_demo --mock     # force mocked generation (no network)

The API key is never printed, logged or written: only whether one is configured.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from types import SimpleNamespace

from . import config

DOCS = os.path.join(config.ROOT, "docs")
RUNS = os.path.join(DOCS, "demo_runs")
REPORT = os.path.join(DOCS, "DEMO_READINESS_VERIFICATION.md")
BEGIN, END = "<!-- BEGIN GENERATED: verify_demo.py -->", "<!-- END GENERATED: verify_demo.py -->"
SOURCE_CORPUS = os.path.join(config.ROOT, "pismo_kb_release_r2", "kb_corpus")
TRANSFERS_OP = "KU-API-core-platform-payment-methods--payment-methods-part-02::op-post-transfers"
EVENT = "platform-authorization-platform-authorization-1"

QUESTIONS = [
    {"id": "Q1", "kind": "Exact error lookup", "q": "What does WEAM0029 mean?",
     "evidence": lambda ev: any(e["ku_id"] == "KU-CHG-2-october-2026" and e["label"] in ("E1", "E2") for e in ev),
     "evidence_desc": "KU-CHG-2-october-2026 passage containing WEAM0029 ranked 1-2",
     "answer": lambda r: r["status"] == "answered" and "WEAM0029" in r["answer"] and re.search(r"removed|no longer|historical|changelog", r["answer"], re.I),
     "answer_desc": "answered; explains WEAM0029 and marks it as removed/historical"},
    {"id": "Q2", "kind": "Documented workflow", "q": "How do I release funds that I previously held on an account?",
     "evidence": lambda ev: any(e["ku_id"] == "KU-PAY-hold-funds" for e in ev) and any("hold-funds-unblock" in e["chunk_id"] for e in ev),
     "evidence_desc": "KU-PAY-hold-funds guide + the post-payments-v1-hold-funds-unblock operation",
     "answer": lambda r: r["status"] == "answered" and "/payments/v1/payments/hold-funds/unblock" in r["answer"],
     "answer_desc": "answered; names POST /payments/v1/payments/hold-funds/unblock"},
    {"id": "Q3", "kind": "Operation-to-event (operationId)", "q": "Which event does post-transfers emit?",
     "evidence": lambda ev: any(e["chunk_id"] == TRANSFERS_OP for e in ev) and any(e["origin"] == "operation_events" and "op-post-transfers" in e["chunk_id"] for e in ev),
     "evidence_desc": "post-transfers operation + its 'Events emitted' table",
     "answer": lambda r: r["status"] == "answered" and EVENT in r["answer"],
     "answer_desc": f"answered; names {EVENT}"},
    {"id": "Q4", "kind": "Operation-to-event (natural language)", "q": "Which event is generated when I create a transfer?",
     "evidence": lambda ev: any(e["chunk_id"] == TRANSFERS_OP for e in ev) and any(e["origin"] == "operation_events" and "op-post-transfers" in e["chunk_id"] for e in ev),
     "evidence_desc": "post-transfers operation (Create transfer) + its 'Events emitted' table",
     "answer": lambda r: r["status"] in ("answered", "partial") and EVENT in r["answer"] and (r.get("verification") or {}).get("operation_alignment"),
     "answer_desc": f"names {EVENT} for POST /payment-methods/v2/transfers, not the transfer-schedule operation"},
    {"id": "Q5", "kind": "Webhook troubleshooting", "q": "How do I verify webhook requests?",
     "evidence": lambda ev: ev and ev[0]["ku_id"] == "KU-EVT-verifying-webhook-requests",
     "evidence_desc": "KU-EVT-verifying-webhook-requests ranked 1",
     "answer": lambda r: r["status"] == "answered" and "JWT" in r["answer"],
     "answer_desc": "answered; JWT verification steps"},
    {"id": "Q6", "kind": "Negative (not documented)", "q": "How do I perform PCI card go-live?",
     "evidence": lambda ev: not any(e["origin"] == "named_operation" for e in ev),
     "evidence_desc": "no evidence documents a PCI card go-live (accounts go-live is only a near-match)",
     "answer": lambda r: r["status"] in ("not_documented", "partial") and not re.search(r"^\s*(use|call)\b[^\n]*go-live", r["answer"], re.I | re.M),
     "answer_desc": "not_documented/partial; does not present accounts go-live as the procedure"},
]


class Recorder:
    """Wraps an OpenAI-compatible client and keeps the exact messages sent."""

    def __init__(self, inner):
        self.inner, self.calls = inner, []
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self._create))

    def _create(self, **kw):
        self.calls.append(kw)
        return self.inner.chat.completions.create(**kw)


class MockClient:
    """Deterministic stand-in used only with --mock or when no key is configured: cites E1 and abstains."""

    def __init__(self):
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self._create))

    def _create(self, **kw):
        body = json.dumps({"status": "not_documented", "answer": "MOCKED generation - no model was called [E1].",
                           "citations": ["E1"], "missing_information": "mocked"})
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=body))])


def run_pytest(path, cwd, name):
    xml = os.path.join(RUNS, f"junit_{name}.xml")
    env = dict(os.environ, HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
    t = time.time()
    p = subprocess.run([sys.executable, "-B", "-s", "-m", "pytest", path, "-q", "-p", "no:cacheprovider", f"--junitxml={xml}"],
                       cwd=cwd, env=env, capture_output=True, text=True)
    root = ET.parse(xml).getroot()
    suite = root if root.tag == "testsuite" else root.find("testsuite")
    a = {k: int(suite.get(k, 0)) for k in ("tests", "failures", "errors", "skipped")}
    failed = [f"{c.get('classname')}::{c.get('name')}" for c in suite.iter("testcase") if c.find("failure") is not None or c.find("error") is not None]
    return {"suite": name, "path": path, **a, "passed": a["tests"] - a["failures"] - a["errors"] - a["skipped"],
            "failed_tests": failed, "returncode": p.returncode, "seconds": round(time.time() - t, 1),
            "last_line": (p.stdout.strip().splitlines() or [""])[-1]}


def run_questions(mock):
    from .generation import OpenAIGenerator, make_openai_client
    from .pipeline import Assistant
    key = bool(os.environ.get("OPENAI_API_KEY", "").strip())
    mode = "mocked" if (mock or not key) else "live"
    rec = Recorder(MockClient() if mode == "mocked" else make_openai_client())
    a = Assistant(generator=OpenAIGenerator(client=rec))
    by_id = {c["chunk_id"]: c for c in a.retriever.chunks}
    out = []
    for spec in QUESTIONS:
        n = len(rec.calls)
        t = time.time()
        r = a.answer(spec["q"])
        secs = round(time.time() - t, 1)
        prompt = rec.calls[n]["messages"][1]["content"] if len(rec.calls) > n else ""
        ev = r["evidence"]
        full_text = all(by_id[e["chunk_id"]]["text"] in prompt for e in ev) if prompt else False
        cites = []
        for c in r["citations"]:
            exists = all(os.path.isfile(os.path.join(SOURCE_CORPUS, s["path"])) and s["url"].startswith("https://") for s in c["sources"])
            cites.append({"label": c["label"], "ku_id": c["ku_id"], "section": c["section"], "origin": c["origin"],
                          "sources_exist": exists, "sources": [s["path"] for s in c["sources"]]})
        ev_ok = bool(spec["evidence"](ev))
        ans_ok = bool(spec["answer"](r)) if mode == "live" else None
        out.append({
            "id": spec["id"], "kind": spec["kind"], "question": spec["q"], "mode": mode, "seconds": secs, "status": r["status"],
            "error": r.get("error"), "model": r.get("model"),
            "top_retrieved": [{"label": e["label"], "chunk_id": e["chunk_id"], "ku_id": e["ku_id"], "title": e["ku_title"],
                               "origin": e["origin"], "reason": e["reason"]} for e in ev],
            "matched_operations": [{k: m.get(k) for k in ("operation", "method", "path", "summary", "matched_by")} for m in r["matched_operations"]],
            "expected_evidence": spec["evidence_desc"], "evidence_ok": ev_ok,
            "full_text_in_prompt": full_text, "prompt_chars": len(prompt), "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()[:16],
            "expected_answer": spec["answer_desc"], "answer_ok": ans_ok, "answer": r["answer"],
            "citations": cites, "citations_valid": r.get("citations_valid"), "verification": r.get("verification"), "warnings": r["warnings"]})
    return mode, out


def before_after_q4():
    p = os.path.join(RUNS, "before_live.json")
    if not os.path.exists(p):
        return None
    b = next((x for x in json.load(open(p, encoding="utf-8")) if x["id"] == "Q4"), None)
    if not b:
        return None
    return {"before_evidence": [f"{e['label']} {e['origin']} {e['chunk_id']}" for e in b["evidence"]],
            "before_status": b["status"], "before_citations_valid": b.get("citations_valid"),
            "before_answer": b["answer"], "post_transfers_in_before_evidence": any(e["chunk_id"] == TRANSFERS_OP for e in b["evidence"])}


def requirement_status(tests, mode, qs):
    tests_ok = all(t["failures"] == 0 and t["errors"] == 0 for t in tests)
    integ = all(q["status"] not in ("generation_error", "no_evidence") and q["full_text_in_prompt"] for q in qs)
    r1 = "verified" if (tests_ok and integ and mode == "live") else ("partially verified" if integ else "unresolved")
    det = all(q["citations_valid"] for q in qs) and all(c["sources_exist"] for q in qs for c in q["citations"])
    r2 = "partially verified" if (det and tests_ok) else "unresolved"   # never 'verified': semantic support is not checked
    r3 = "verified" if all(q["evidence_ok"] for q in qs) and (mode != "live" or all(q["answer_ok"] for q in qs)) else "unresolved"
    if mode != "live" and r3 == "verified":
        r3 = "partially verified"
    return {"1. Retrieval-to-answer integration": r1, "2. Citation correctness": r2, "3. Demo-blocking chunking/retrieval/evidence defects": r3}


def markdown(summary):
    s = summary
    L = [f"_Generated {s['generated_at']} by `python -B -s -m pismo_assistant.verify_demo` - generation was **{s['mode'].upper()}**"
         f"{' (model ' + s['model'] + ')' if s['model'] else ''}._", "", "### Requirement status", "", "| Requirement | Status |", "| --- | --- |"]
    L += [f"| {k} | **{v}** |" for k, v in s["requirements"].items()]
    L += ["", "### Test runs", "", "| Suite | Tests | Passed | Failed | Errors | Skipped |", "| --- | ---: | ---: | ---: | ---: | ---: |"]
    L += [f"| `{t['path']}` | {t['tests']} | {t['passed']} | {t['failures']} | {t['errors']} | {t['skipped']} |" for t in s["tests"]]
    L += ["", "### Demo questions", ""]
    for q in s["questions"]:
        v = q["verification"] or {}
        L += [f"#### {q['id']} - {q['kind']}: \"{q['question']}\"", "",
              f"- Status: `{q['status']}` ({q['mode']}, {q['seconds']} s); expected evidence ({q['expected_evidence']}): **{'yes' if q['evidence_ok'] else 'NO'}**; "
              f"expected answer ({q['expected_answer']}): **{ {True: 'yes', False: 'NO', None: 'not judged (mocked)'}[q['answer_ok']] }**",
              f"- Complete passage text in prompt: **{'yes' if q['full_text_in_prompt'] else 'NO'}** ({q['prompt_chars']} chars)",
              f"- Matched operations: {', '.join(m['operation'] + ' via ' + m['matched_by'] for m in q['matched_operations']) or 'none'}",
              f"- Citation checks: valid={q['citations_valid']}; " + ", ".join(f"{k}={v[k]}" for k in v),
              f"- Warnings: {q['warnings'] or 'none'}", "", "| Label | Origin | Chunk | KU title |", "| --- | --- | --- | --- |"]
        L += [f"| {e['label']} | {e['origin']} | `{e['chunk_id']}` | {e['title']} |" for e in q["top_retrieved"]]
        L += ["", "Cited: " + (", ".join(f"{c['label']} -> {c['ku_id']} / {c['section']} ({'; '.join(c['sources'])})" for c in q["citations"]) or "none"), "",
              "<details><summary>Answer</summary>", "", q["answer"] or "(none)", "", "</details>", ""]
    ba = s.get("before_after_q4")
    if ba:
        L += ["### Q4 before/after (captured live before the fix: `docs/demo_runs/before_live.json`)", "",
              f"- Before: status `{ba['before_status']}`, citations_valid `{ba['before_citations_valid']}`, post-transfers in evidence: **{ba['post_transfers_in_before_evidence']}**",
              "- Before evidence: " + "; ".join(f"`{x}`" for x in ba["before_evidence"]),
              f"- Before answer: {ba['before_answer']}", ""]
    return "\n".join(L)


def print_summary(s):
    w = print
    w("\n" + "=" * 100)
    w(f"DEMO READINESS VERIFICATION  -  generation: {s['mode'].upper()}{' (' + s['model'] + ')' if s['model'] else ''}  -  key configured: {s['key_configured']} (value never shown)")
    w("=" * 100)
    for k, v in s["requirements"].items():
        w(f"  {k:60} {v.upper()}")
    w("\nTESTS")
    for t in s["tests"]:
        w(f"  {t['path']:45} {t['tests']:3} tests | {t['passed']} passed | {t['failures']} failed | {t['errors']} errors | {t['skipped']} skipped")
        for f in t["failed_tests"]:
            w(f"      FAILED {f}")
    w("\nDEMO QUESTIONS")
    for q in s["questions"]:
        v = q["verification"] or {}
        aok = {True: "yes", False: "NO", None: "n/a (mocked)"}[q["answer_ok"]]
        w(f"  {q['id']} {q['kind']}: \"{q['question']}\"")
        w(f"     status={q['status']}  evidence_ok={'yes' if q['evidence_ok'] else 'NO'}  answer_ok={aok}  full_text_in_prompt={'yes' if q['full_text_in_prompt'] else 'NO'}  {q['seconds']}s")
        w(f"     top: " + " | ".join(f"{e['label']} {e['chunk_id'][:70]}" for e in q["top_retrieved"][:3]))
        named = [e for e in q["top_retrieved"] if e["origin"] in ("named_operation", "operation_events")]
        if named:
            w(f"     added: " + " | ".join(f"{e['label']} {e['origin']} {e['chunk_id'][-45:]}" for e in named))
        w(f"     citations: " + (", ".join(f"{c['label']}->{c['ku_id']}" for c in q["citations"]) or "none")
          + f"  | checks: valid={q['citations_valid']} " + " ".join(f"{k}={'ok' if v[k] else 'FAIL'}" for k in v if k != 'semantic_support_verified')
          + " semantic=NOT VERIFIED")
        for wn in q["warnings"]:
            w(f"     WARNING: {wn[:200]}")
        w(f"     answer: {(q['answer'] or '').strip().replace(chr(10), ' ')[:260]}")
    ba = s.get("before_after_q4")
    if ba:
        w("\nQ4 BEFORE (captured live before the fix) vs AFTER")
        w(f"  before: status={ba['before_status']} citations_valid={ba['before_citations_valid']} post-transfers in evidence={ba['post_transfers_in_before_evidence']}")
        w(f"  before answer: {ba['before_answer'][:220]}")
        q4 = next(q for q in s["questions"] if q["id"] == "Q4")
        w(f"  after:  status={q4['status']} citations_valid={q4['citations_valid']} post-transfers in evidence={any(e['chunk_id'] == TRANSFERS_OP for e in q4['top_retrieved'])}")
    w("\nCOMMANDS")
    w("  app:    python -B -s -m pismo_assistant \"How do I release funds that I previously held on an account?\"")
    w("  verify: python -B -s -m pismo_assistant.verify_demo")
    w("  tests:  python -B -s -m pytest pismo_assistant/tests -q -p no:cacheprovider")
    w("          (cd pismo_full_corpus_retrieval_experiment; python -B -s -m pytest tests -q -p no:cacheprovider)")
    w(f"  report: docs/DEMO_READINESS_VERIFICATION.md  | raw results: docs/demo_runs/verification_results.json")
    w("=" * 100)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--mock", action="store_true")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    os.makedirs(RUNS, exist_ok=True)
    tests = [run_pytest("pismo_assistant/tests", config.ROOT, "assistant"),
             run_pytest("tests", config.EXPERIMENT, "experiment")]
    tests[1]["path"] = "pismo_full_corpus_retrieval_experiment/tests"
    mode, qs = run_questions(a.mock)
    summary = {"generated_at": time.strftime("%Y-%m-%d %H:%M:%S"), "mode": mode,
               "model": next((q["model"] for q in qs if q.get("model")), None) if mode == "live" else None,
               "key_configured": bool(os.environ.get("OPENAI_API_KEY", "").strip()), "tests": tests, "questions": qs,
               "before_after_q4": before_after_q4()}
    summary["requirements"] = requirement_status(tests, mode, qs)
    with open(os.path.join(RUNS, "verification_results.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=1)
    if os.path.exists(REPORT):
        doc = open(REPORT, encoding="utf-8").read()
        if BEGIN in doc and END in doc:
            doc = doc.split(BEGIN)[0] + BEGIN + "\n" + markdown(summary) + "\n" + END + doc.split(END, 1)[1]
            with open(REPORT, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(doc)
    print_summary(summary)
    return 0 if all(v != "unresolved" for v in summary["requirements"].values()) else 1


if __name__ == "__main__":
    sys.exit(main())
