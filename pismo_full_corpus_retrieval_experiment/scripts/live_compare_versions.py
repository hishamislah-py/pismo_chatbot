"""LIVE end-to-end comparison of v1, v1.1 and v1.2: the same questions through the production answer pipeline
(Assistant.answer: evidence -> OpenAI generation -> citation validation) with each version's own evidence.

Isolation: every index is loaded in this process only (served paths in pismo_assistant/config.py are not changed; each
candidate is integrity-checked against its own KU collection). No database, no server, no router classifier. The
generator is the backend's (make_budgeted_generator) with the backend's settings (model, per-attempt timeout, retries).
The API key is never printed. Results are appended to <out.jsonl> (one line per answer), so a rerun resumes.

Usage: python -B -E -s scripts/live_compare_versions.py <retrieval.json> <out.jsonl> [--workers N] [--repeats-webhook N]
"""
import argparse
import json
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", DATABASE_URL="sqlite://", ROUTER_ENABLED="false")
from dotenv import dotenv_values  # noqa: E402
_KEY = (os.environ.get("OPENAI_API_KEY") or dotenv_values(os.path.join(os.path.dirname(os.path.dirname(HERE)), ".env"))
        .get("OPENAI_API_KEY") or "").strip()   # read before the offline modules blank it; never printed
import compare_versions as cv  # noqa: E402  (sets OPENAI_API_KEY="" for its own offline use)
import compare_candidate as cc  # noqa: E402
os.environ["OPENAI_API_KEY"] = _KEY
from backend.app.core.config import get_settings  # noqa: E402
from backend.app.services.assistant_service import make_budgeted_generator  # noqa: E402

WEBHOOK_SETS = ("regression_v1", "regression_v2", "probe")
WEBHOOK_FROZEN = {"D2", "D5", "DG07"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("retrieval_json")
    ap.add_argument("out_jsonl")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--repeats-webhook", type=int, default=2)
    ap.add_argument("--limit", type=int, default=None, help="make at most N answer calls (smoke test)")
    args = ap.parse_args()
    if not os.environ.get("OPENAI_API_KEY", "").strip():
        sys.exit("no API key available; stopping before any live call")
    ret = json.load(open(args.retrieval_json, encoding="utf-8"))
    s = get_settings()
    gen_settings = {"model": s.openai_model, "attempt_timeout_s": s.llm_attempt_timeout_s, "max_retries": s.openai_max_retries,
                    "response_format": "json_object", "prompt": "pismo_assistant.generation.SYSTEM_PROMPT (unchanged)"}
    print("generation settings:", gen_settings, "| key present: True")

    # one task per (version, unique question, repeat)
    questions = {}
    for set_name, rows in ret["versions"]["v1"]["questions"].items():
        for r in rows:
            q = questions.setdefault(r["question"], {"question": r["question"], "refs": [], "webhook": False})
            q["refs"].append(f"{set_name}:{r['id']}")
            q["webhook"] |= set_name in WEBHOOK_SETS or r["id"] in WEBHOOK_FROZEN
    done = set()
    if os.path.exists(args.out_jsonl):
        for l in open(args.out_jsonl, encoding="utf-8"):
            d = json.loads(l)
            done.add((d["version"], d["question"], d["repeat"]))

    embedder, assistants = None, {}
    for name, (idx, mig) in cv.VERSIONS.items():
        a = cc.load(os.path.join(idx, "chunks.jsonl"), os.path.join(idx, "corpus_summary.json"), os.path.join(idx, "embeddings"), mig,
                    embedder=embedder)
        embedder = a.retriever.embedder
        assert a.retriever.chunk_set_hash == ret["versions"][name]["chunk_set_hash"], f"{name}: index differs from the retrieval run"
        a.generator = make_budgeted_generator(s.llm_attempt_timeout_s, s.openai_max_retries)
        # evidence is deterministic: compute once, check it against the retrieval run, then serve it to answer()
        expected = {r["question"]: [e["chunk_id"] for e in r["evidence"]] for rows in ret["versions"][name]["questions"].values() for r in rows}
        cache = {}
        for qt in questions:
            t = time.perf_counter()
            ev = a.evidence(qt)
            cache[qt] = (ev, round((time.perf_counter() - t) * 1000))
            assert [e.chunk_id for e in ev] == expected[qt], f"{name}: evidence for {qt!r} differs from the retrieval run"
        a.evidence = lambda q, _c=cache: _c[q][0]
        assistants[name] = (a, cache)
        print(f"{name}: index {a.retriever.chunk_set_hash[:12]} loaded, evidence for {len(cache)} questions verified")

    calls, lock = [], threading.Lock()
    for name, (a, _) in assistants.items():
        client = a.generator.client
        original = client.chat.completions.create

        def counted(_orig=original, _name=name, **kw):
            rec = {"version": _name, "ok": False}
            t0 = time.perf_counter()
            try:
                r = _orig(**kw)
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
                with lock:
                    calls.append(rec)
                threading.current_thread().last_call = rec
        client.chat.completions.create = counted

    tasks = [(name, qt, rep) for qt, q in questions.items() for rep in range(args.repeats_webhook if q["webhook"] else 1)
             for name in assistants if (name, qt, rep) not in done][:args.limit]
    print(f"{len(tasks)} live answer calls to make ({len(done)} already done)")

    def run(task):
        name, qt, rep = task
        a, cache = assistants[name]
        threading.current_thread().last_call = None
        t = time.perf_counter()
        res = a.answer(qt)
        total = round((time.perf_counter() - t) * 1000)
        call = getattr(threading.current_thread(), "last_call", None)
        return {"version": name, "chunk_set_hash": a.retriever.chunk_set_hash, "question": qt, "refs": questions[qt]["refs"],
                "repeat": rep, "generation": gen_settings, "retrieval_ms": cache[qt][1], "answer_ms": total, "call": call,
                "evidence": [(e.label, e.chunk_id, e.origin) for e in cache[qt][0]],
                **{k: res.get(k) for k in ("status", "answer", "missing_information", "warnings", "citations_valid", "verification",
                                           "error", "model")},
                "citations": [{"label": c["label"], "chunk_id": c["chunk_id"], "ku_id": c["ku_id"]} for c in res.get("citations") or []]}

    n = 0
    with open(args.out_jsonl, "a", encoding="utf-8") as fh, ThreadPoolExecutor(args.workers) as pool:
        for fut in as_completed([pool.submit(run, t) for t in tasks]):
            try:
                rec = fut.result()
            except Exception as e:  # infrastructure failure: recorded, run continues
                print("task failed:", type(e).__name__, str(e)[:200])
                continue
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            n += 1
            if n % 25 == 0:
                print(f"{time.strftime('%H:%M:%S')} {n}/{len(tasks)} answers; calls so far {len(calls)}, failed calls {sum(not c['ok'] for c in calls)}")
    print(f"done: {n} answers written; {len(calls)} API calls ({sum(not c['ok'] for c in calls)} failed)")


if __name__ == "__main__":
    main()
