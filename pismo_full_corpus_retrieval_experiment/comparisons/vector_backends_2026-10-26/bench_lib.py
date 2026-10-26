"""Shared code for the NumPy vs FAISS vs Chroma dense-backend comparison (benchmark only, read-only on every input).

The production retriever (pismo_assistant.retrieval.HybridRetriever) and evidence assembly (pipeline.Assistant.evidence)
are used unchanged. BackendRetriever subclasses HybridRetriever and replaces only the dense ranking step; BM25, weighted
RRF (2:1, k=60), exact-identifier promotion, navigation exclusion, webhook scoping and evidence expansion are the
production code paths. Runs under the global interpreter (numpy, faiss) and under the isolated Chroma venv; neither
needs the embedder at query time because query vectors are computed once by the production embedder (embed_queries.py).
"""
import hashlib
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(os.path.dirname(HERE))
ROOT = os.path.dirname(EXP)
OUT = os.path.join(HERE, "out")
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from pismo_assistant import config  # noqa: E402

config.ensure_experiment_on_path()
from common import read_jsonl, sha_file, sha_json  # noqa: E402
from labels import chunk_satisfies, label_key  # noqa: E402
from retrievers import Dense, detect_identifiers, exact_rerank, rank_by_score, rrf  # noqa: E402

from pismo_assistant.retrieval import HybridRetriever  # noqa: E402

EMB_DIR = config.EMBEDDINGS_DIR
VECTORS = os.path.join(EMB_DIR, "window_vectors.npy")
WINDOW_CHUNK = os.path.join(EMB_DIR, "window_chunk.npy")
EXPECTED_CHUNK_SET_HASH = "8db472c58e43022e7a4c8b6240c836476bad08a809cc5a76ee406efaa9a77826"
EXPECTED_VECTORS_SHA = "9c8b25161ed60bda8d4d2e70958aa399ec1a4aa4a23f6bbec25774afcffa53bc"
EXPECTED_WINDOW_CHUNK_SHA = "5ead2ab9369d42e55b0329e8cadde7c4b3c591ed30265b0ecb805178bd94912e"
QUERY_VECTORS = os.path.join(OUT, "query_vectors.npz")
os.makedirs(OUT, exist_ok=True)
DEPTHS = (100, 500, 2000)   # truncated dense window depths (requirement 5); None = full ranking of all 25,325 windows


def dump(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def dir_size(path):
    return sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(path) for f in fs)


def verify_embedding_files():
    """The exact on-disk artefacts production loads; stops on any mismatch (stale or different index)."""
    got = {"window_vectors.npy": sha_file(VECTORS), "window_chunk.npy": sha_file(WINDOW_CHUNK)}
    want = {"window_vectors.npy": EXPECTED_VECTORS_SHA, "window_chunk.npy": EXPECTED_WINDOW_CHUNK_SHA}
    if got != want:
        raise SystemExit(f"embedding files differ from the audited artefacts: {got}")
    return got


# ---------------------------------------------------------------- evaluation questions (existing assets only)
def load_question_sets(chunks):
    """Labelled sets: benchmark primary/extension (frozen, hash-checked), audit diagnostic (DG01-10), webhook regression
    v2 (RW2, hash-checked). Unlabelled: probe questions and the 6 demo checks (predicate checks, not metrics)."""
    bench = load(os.path.join(EXP, "BENCHMARK.json"))
    frozen = open(os.path.join(EXP, "BENCHMARK.sha256"), encoding="utf-8").read().split()[0]
    if sha_json({"primary": bench["primary"], "extension": bench["extension"]}) != frozen:
        raise SystemExit("FROZEN BENCHMARK HASH MISMATCH")
    from pismo_assistant.audit_retrieval import resolve_diagnostic
    rw_path = os.path.join(EXP, "benchmark_inputs", "regression_webhook_auth_v2.json")
    rw_sha = open(rw_path[:-5] + ".sha256", encoding="utf-8").read().split()[0]
    if sha_file(rw_path) != rw_sha:
        raise SystemExit("regression_webhook_auth_v2.json differs from its frozen sha256")
    rw = load(rw_path)
    webhook = []
    for q in rw["questions"]:
        labels = []
        for l in q["expected"]:
            ids = [c["chunk_id"] for c in chunks if chunk_satisfies(c, l)]
            labels.append({"key": label_key(l), "status": "valid" if ids else "no_matching_chunk", "relevant_chunk_ids": ids,
                           "relevant_ku_ids": sorted({c.split("::")[0] for c in ids})})
        webhook.append({"id": q["id"], "set": "webhook_v2", "q": q["q"], "type": q.get("type"), "workflow": q.get("cat"),
                        "answerability": q.get("answerability"), "labels": labels,
                        "scored": any(l["status"] == "valid" for l in labels)})
    diag = resolve_diagnostic(chunks)
    probes = load(os.path.join(EXP, "benchmark_inputs", "probe_questions_unlabelled_v1.json"))["questions"]
    from pismo_assistant.verify_demo import QUESTIONS as DEMO
    labelled = bench["primary"] + bench["extension"] + diag + webhook
    unlabelled = ([{"id": p["id"], "set": "probe", "q": p["q"], "kind": p.get("kind")} for p in probes]
                  + [{"id": "DEMO-" + d["id"], "set": "demo", "q": d["q"], "kind": d["kind"]} for d in DEMO])
    return {"labelled": labelled, "unlabelled": unlabelled, "benchmark_sha256": frozen, "webhook_v2_sha256": rw_sha,
            "demo": DEMO}


EDGE_QUESTIONS = [  # retrieval-level edge cases (behaviour checks, no labels)
    {"id": "EDGE-empty", "q": ""},
    {"id": "EDGE-blank", "q": "   "},
    {"id": "EDGE-unknown-error", "q": "What does error ZQXW9917 mean?"},
    {"id": "EDGE-unknown-op", "q": "What does post-quantum-ledger-teleport-v9 do?"},
    {"id": "EDGE-unknown-path", "q": "POST /v9/nonexistent/teleport-balance"},
]


# ---------------------------------------------------------------- dense backends (window search -> chunk ranking)
def chunk_order_from_windows(win_idx, win_scores, window_chunk, ids, n_chunks, full):
    """Chunk score = max over its windows (production Dense.scores). Full: every chunk ranked exactly as production
    (rank_by_score over all chunks, -1.0 for chunks without a scored window). Truncated: only chunks with a window in
    the returned list, same (-score, chunk id) ordering."""
    out = np.full(n_chunks, -1.0, dtype=np.float64)
    np.maximum.at(out, window_chunk[win_idx], win_scores.astype(np.float32))
    if full:
        return rank_by_score(out, ids)
    present = np.unique(window_chunk[win_idx])
    return sorted(present.tolist(), key=lambda i: (-out[i], ids[i]))


class NumpyDense:
    name = "numpy"

    def __init__(self, vectors, window_chunk, ids):
        self.dense = Dense(vectors, window_chunk, len(ids))
        self.ids = ids

    def order(self, qv):
        return rank_by_score(self.dense.scores(qv), self.ids)   # production: retrieval.HybridRetriever.ranked


class FaissDense:
    def __init__(self, index, window_chunk, ids, depth=None):
        self.index, self.wc, self.ids, self.depth = index, window_chunk, ids, depth
        self.name = "faiss_flat" + (f"@{depth}" if depth else "")

    def search(self, qv):
        k = self.depth or self.index.ntotal
        D, I = self.index.search(np.ascontiguousarray(qv.reshape(1, -1), dtype=np.float32), k)
        keep = I[0] >= 0
        return I[0][keep], D[0][keep]

    def order(self, qv):
        wi, ws = self.search(qv)
        return chunk_order_from_windows(wi, ws, self.wc, self.ids, len(self.ids), full=self.depth is None)


class ChromaDense:
    """Cosine collection; similarity = 1 - distance. Window id 'w%05d' = row of window_vectors.npy."""

    def __init__(self, collection, window_chunk, ids, depth=None):
        self.col, self.wc, self.ids, self.depth = collection, window_chunk, ids, depth
        self.n_windows = len(window_chunk)
        self.name = "chroma" + (f"@{depth}" if depth else "_full")

    def search(self, qv):
        r = self.col.query(query_embeddings=[qv.astype(np.float32).tolist()], n_results=self.depth or self.n_windows,
                           include=["distances"])
        wi = np.fromiter((int(x[1:]) for x in r["ids"][0]), dtype=np.int64)
        return wi, 1.0 - np.asarray(r["distances"][0], dtype=np.float64)

    def order(self, qv):
        wi, ws = self.search(qv)
        # full: a chunk missing from an incomplete HNSW result keeps -1.0 and stays ranked (tail), exactly like a
        # full-depth exact ranking would; recorded separately as hnsw_returned
        return chunk_order_from_windows(wi, ws, self.wc, self.ids, len(self.ids), full=self.depth is None)


# ---------------------------------------------------------------- retriever with a pluggable dense step
class CachedEmbedder:
    """Returns the production embedder's vector for a question (computed once by embed_queries.py)."""

    def __init__(self, path=QUERY_VECTORS):
        z = np.load(path, allow_pickle=False)
        self.vec = {q: v for q, v in zip(z["questions"].tolist(), z["vectors"])}

    def encode(self, texts, **kw):
        return np.stack([self.vec[t] for t in texts])


class BackendRetriever(HybridRetriever):
    """HybridRetriever with `ranked` split into timed parts; only the dense ranking comes from `self.backend`.
    The lines below mirror HybridRetriever.ranked exactly (checked by step0_reproduce.py / run_backend.py)."""

    def __init__(self, backend=None, **kw):
        super().__init__(**kw)
        self.backend = backend or NumpyDense(self.dense.V, self.dense.wc, self.ids)
        self.last = None

    def parts(self, question):
        if not question or not question.strip():
            return {"order": [], "n_exact": 0, "b_order": [], "d_order": [], "t": {}}
        t0 = time.perf_counter()
        qv = self.embedder.encode([question], normalize_embeddings=True, convert_to_numpy=True)[0]
        t1 = time.perf_counter()
        b_order = rank_by_score(self.bm25.scores(question), self.ids, positive_only=True)
        t2 = time.perf_counter()
        d_order = self.backend.order(qv)
        t3 = time.perf_counter()
        fused = rrf([b_order, d_order], list(config.RRF_WEIGHTS), self.ids)
        idents = detect_identifiers(question)
        order, n_exact = exact_rerank(fused, self.texts_lower, idents)
        t4 = time.perf_counter()
        return {"order": order, "n_exact": n_exact, "b_order": b_order, "d_order": d_order,
                "t": {"embed_lookup": t1 - t0, "bm25": t2 - t1, "dense": t3 - t2, "fusion": t4 - t3}}

    def ranked(self, question):
        p = self.parts(question)
        self.last = p
        return p["order"], p["n_exact"]


def sha_list(xs):
    return hashlib.sha256("\n".join(map(str, xs)).encode()).hexdigest()[:16]
