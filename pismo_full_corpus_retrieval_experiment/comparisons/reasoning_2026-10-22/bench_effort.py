"""Part 1 - benchmark arm comparison of the answer model's reasoning effort: production default (no reasoning_effort
sent) vs "low". Served v1 index, current code, evidence computed ONCE per question and shared by both arms, so the only
difference between arms is the reasoning_effort parameter of the answer call. Isolated: nothing in the running app or
its configuration is changed. The API key is never printed.

Usage: python -B -E -s bench_effort.py <out.jsonl> [--workers N] [--limit N]
"""
import argparse
import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(os.path.dirname(HERE))
ROOT = os.path.dirname(EXP)
sys.path[:0] = [os.path.join(EXP, "scripts"), ROOT]
os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", DATABASE_URL="sqlite://", ROUTER_ENABLED="false")
from dotenv import dotenv_values  # noqa: E402
KEY = (os.environ.get("OPENAI_API_KEY") or dotenv_values(os.path.join(ROOT, ".env")).get("OPENAI_API_KEY") or "").strip()
import common  # noqa: E402
import compare_candidate as cc  # noqa: E402  (sets OPENAI_API_KEY="" for its offline use)
from pismo_assistant import audit_retrieval as ar, config  # noqa: E402
os.environ["OPENAI_API_KEY"] = KEY
from backend.app.core.config import get_settings  # noqa: E402
from backend.app.services.assistant_service import make_budgeted_generator  # noqa: E402
from pismo_assistant.pipeline import Assistant  # noqa: E402

ARMS = {"default": None, "low": "low"}


def arm_generator(effort, settings, calls):
    gen = make_budgeted_generator(settings.llm_attempt_timeout_s, settings.openai_max_retries)
    client = gen.client
    original = client.chat.completions.create

    def create(**kw):
        if effort:
            kw["reasoning_effort"] = effort           # the ONLY difference between the arms
        rec = {"ok": False}
        t0 = time.perf_counter()
        try:
            r = original(**kw)
            rec["ok"] = True
            u = getattr(r, "usage", None)
            if u is not None:
                det = getattr(u, "completion_tokens_details", None)
                rec.update(prompt_tokens=u.prompt_tokens, completion_tokens=u.completion_tokens,
                           reasoning_tokens=getattr(det, "reasoning_tokens", None) if det else None)
            return r
        except Exception as e:
            rec["error"] = type(e).__name__
            raise
        finally:
            rec["ms"] = round((time.perf_counter() - t0) * 1000)
            calls.append(rec)
            threading.current_thread().last_call = rec
    client.chat.completions.create = create
    return gen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    assert KEY, "no API key"
    s = get_settings()
    base = Assistant()                                        # served v1 index (pismo_assistant/config.py paths)
    by_id = {c["chunk_id"]: c for c in base.retriever.chunks}
    bench = common.load_json(ar.BENCHMARK)
    sets = {"frozen": bench["primary"] + bench["extension"] + ar.resolve_diagnostic(base.retriever.chunks)}
    for name, f in (("regression_v1", "regression_webhook_auth_v1.json"), ("regression_v2", "regression_webhook_auth_v2.json")):
        sets[name] = cc.regression_questions(os.path.join(EXP, "benchmark_inputs", f), base.retriever.chunks)
    questions, meta = {}, {}
    for sname, qs in sets.items():
        for q in qs:
            m = ar.evaluate_question(q, base, by_id)           # labels and evidence relevance (no model call)
            questions.setdefault(q["q"], [])
            questions[q["q"]].append({"set": sname, "id": q["id"], "answerability": q.get("answerability"),
                                      "evidence_label_recall": m["evidence_label_recall"],
                                      "relevant_chunks": [e["chunk_id"] for e in m["evidence"] if e["relevant"]]})
    cache = {}
    for qt in questions:
        t = time.perf_counter()
        cache[qt] = (base.evidence(qt), round((time.perf_counter() - t) * 1000, 1))
    calls = []
    arms = {}
    for arm, effort in ARMS.items():
        asst = Assistant(retriever=base.retriever, generator=arm_generator(effort, s, calls), op_index=base.op_index)
        asst.evidence = lambda q: cache[q][0]                  # identical evidence for both arms
        arms[arm] = asst
    done = set()
    if os.path.exists(a.out):
        done = {(json.loads(l)["arm"], json.loads(l)["question"]) for l in open(a.out, encoding="utf-8")}
    order = list(questions)
    tasks = [(arm, q) for i, q in enumerate(order) for arm in (ARMS if i % 2 == 0 else reversed(list(ARMS)))
             if (arm, q) not in done][:a.limit]
    print(f"index {base.retriever.chunk_set_hash[:12]} | {len(questions)} unique questions | {len(tasks)} answer calls | "
          f"model {s.openai_model}, attempt timeout {s.llm_attempt_timeout_s}s, retries {s.openai_max_retries}")

    def run(task):
        arm, q = task
        threading.current_thread().last_call = None
        t = time.perf_counter()
        r = arms[arm].answer(q)
        return {"arm": arm, "question": q, "refs": questions[q], "retrieval_ms": cache[q][1],
                "pipeline_ms": round((time.perf_counter() - t) * 1000), "call": threading.current_thread().last_call,
                "evidence": [(e.label, e.chunk_id) for e in cache[q][0]], "evidence_text_sha": hash("".join(e.text for e in cache[q][0])),
                **{k: r.get(k) for k in ("status", "answer", "missing_information", "warnings", "citations_valid", "verification", "error", "model")},
                "citations": [c["chunk_id"] for c in r.get("citations") or []]}
    n = 0
    with open(a.out, "a", encoding="utf-8") as fh, ThreadPoolExecutor(a.workers) as pool:
        for fut in as_completed([pool.submit(run, t) for t in tasks]):
            try:
                fh.write(json.dumps(fut.result(), ensure_ascii=False) + "\n")
                fh.flush()
                n += 1
            except Exception as e:
                print("task failed:", type(e).__name__, str(e)[:200])
            if n and n % 25 == 0:
                print(f"{time.strftime('%H:%M:%S')} {n}/{len(tasks)}; failed API calls so far {sum(not c['ok'] for c in calls)}")
    print(f"done: {n} answers; {len(calls)} API calls ({sum(not c['ok'] for c in calls)} failed)")


if __name__ == "__main__":
    main()
