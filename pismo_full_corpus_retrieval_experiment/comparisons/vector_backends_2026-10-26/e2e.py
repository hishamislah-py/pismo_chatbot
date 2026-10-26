"""End-to-end (live OpenAI) for the 6 demo questions, per dense configuration, in-process (no HTTP API: the API persists
sessions/messages to the dev PostgreSQL database, which this benchmark must not write to).

Same model (OPENAI_MODEL), prompt (generation.build_messages), reasoning effort (OPENAI_REASONING_EFFORT, as the backend
sends it) and citation validation as production. Each question runs once per configuration, sequentially. The API key is
read from the environment / .env by the production code and never printed or stored.

    python -B -s e2e.py --backend numpy
    python -B -s e2e.py --backend faiss --configs faiss_flat
    %USERPROFILE%\\.venvs\\pismo_chroma_bench\\Scripts\\python -B -s e2e.py --backend chroma --configs chroma_full chroma@2000
"""
import argparse
import hashlib
import json
import os
import sys
import time

from bench_lib import OUT, BackendRetriever, CachedEmbedder, NumpyDense, dump, load_question_sets
from pismo_assistant import config
from pismo_assistant.generation import OpenAIGenerator, build_messages
from pismo_assistant.pipeline import Assistant


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=("numpy", "faiss", "chroma"), required=True)
    ap.add_argument("--configs", nargs="*", default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    from run_backend import make_configs, open_backend
    base = BackendRetriever(embedder=CachedEmbedder())
    sets = load_question_sets(base.chunks)
    if a.backend == "numpy":
        cfgs = [NumpyDense(base.dense.V, base.dense.wc, base.ids)]
    else:
        h, _ = open_backend(a.backend)
        cfgs = [c for c in make_configs(a.backend, h, base.ids) if a.configs is None or c.name in a.configs]
    effort = (os.environ.get("OPENAI_REASONING_EFFORT") or "").strip().lower() or None
    rows = []
    for c in cfgs:
        br = BackendRetriever(backend=c, embedder=base.embedder)
        gen = OpenAIGenerator(model=config.OPENAI_MODEL, reasoning_effort=effort)
        asst = Assistant(retriever=br, generator=gen)
        for spec in sets["demo"]:
            q = spec["q"]
            t0 = time.perf_counter()
            ev = asst.evidence(q)
            t_ret = time.perf_counter() - t0
            prompt_sha = hashlib.sha256(json.dumps(build_messages(q, ev), ensure_ascii=False).encode()).hexdigest()[:16]
            # timed generation = the production answer() call minus its own retrieval (measured separately above)
            t1 = time.perf_counter()
            r = asst.answer(q)
            t_answer = time.perf_counter() - t1
            evd = r["evidence"]
            rows.append({"config": c.name, "id": spec["id"], "kind": spec["kind"], "question": q, "status": r["status"],
                         "error": r.get("error"), "model": r.get("model"), "reasoning_effort": effort,
                         "evidence_ids": [e["chunk_id"] for e in evd], "prompt_sha256_16": prompt_sha,
                         "evidence_ok": bool(spec["evidence"](evd)), "expected_evidence": spec["evidence_desc"],
                         "answer_ok": bool(spec["answer"](r)) if r["status"] not in ("generation_error",) else False,
                         "expected_answer": spec["answer_desc"], "citations_valid": r.get("citations_valid"),
                         "n_citations": len(r.get("citations") or []), "warnings": r["warnings"], "answer": r["answer"],
                         "retrieval_s": round(t_ret, 4), "answer_call_s": round(t_answer, 3),
                         "generation_s_est": round(t_answer - t_ret, 3)})
            x = rows[-1]
            print(f"{c.name:14} {spec['id']} status={x['status']:16} evidence_ok={x['evidence_ok']} answer_ok={x['answer_ok']} "
                  f"citations_valid={x['citations_valid']} warnings={len(x['warnings'])} total={x['answer_call_s']}s prompt={prompt_sha}")
    path = os.path.join(OUT, f"e2e_{a.backend}.json")
    dump(path, {"generated_at": time.strftime("%Y-%m-%d %H:%M:%S"), "model": config.OPENAI_MODEL, "reasoning_effort": effort,
                "rows": rows})


if __name__ == "__main__":
    main()
