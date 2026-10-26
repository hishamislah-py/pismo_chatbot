"""Build the benchmark's persistent dense indexes from the existing production vectors (no re-embedding).

    python -B -s build_indexes.py --backend faiss                                    # global interpreter
    %USERPROFILE%\\.venvs\\pismo_chroma_bench\\Scripts\\python -B -s build_indexes.py --backend chroma

FAISS: IndexFlatIP over the 25,325 L2-normalised float32 windows (inner product == cosine), out/faiss/flat_ip.index.
Chroma: persistent client at out/chroma_db, collection pismo_windows_v1, hnsw space=cosine (defaults otherwise), ids
'w%05d' = row of window_vectors.npy, metadata {chunk_id, chunk_index, window_ordinal}. Refuses to overwrite an existing
index: delete only this benchmark's out/ folder to rebuild.
"""
import argparse
import os
import platform
import sys
import time

import numpy as np
import psutil

from bench_lib import EXPECTED_CHUNK_SET_HASH, OUT, VECTORS, WINDOW_CHUNK, dir_size, dump, read_jsonl, verify_embedding_files
from pismo_assistant import config

CHROMA_DIR = os.path.join(OUT, "chroma_db")
CHROMA_COLLECTION = "pismo_windows_v1"
FAISS_PATH = os.path.join(OUT, "faiss", "flat_ip.index")
BATCH = 5000


def build_faiss(V, meta):
    import faiss
    if os.path.exists(FAISS_PATH):
        raise SystemExit(f"{FAISS_PATH} exists; refusing to overwrite")
    os.makedirs(os.path.dirname(FAISS_PATH), exist_ok=True)
    t = time.perf_counter()
    index = faiss.IndexFlatIP(V.shape[1])
    index.add(V)
    t_add = time.perf_counter() - t
    faiss.write_index(index, FAISS_PATH)
    t_total = time.perf_counter() - t
    meta.update(library="faiss", version=faiss.__version__, index_type="IndexFlatIP", metric="inner product (== cosine on unit vectors)",
                ntotal=int(index.ntotal), d=int(index.d), add_seconds=round(t_add, 3), build_and_write_seconds=round(t_total, 3),
                omp_threads=faiss.omp_get_max_threads(), path=os.path.relpath(FAISS_PATH, OUT), size_bytes=os.path.getsize(FAISS_PATH))
    dump(FAISS_PATH + ".meta.json", meta)
    return meta


def build_chroma(V, wc, meta):
    import chromadb
    from chromadb.config import Settings
    if os.path.exists(CHROMA_DIR):
        raise SystemExit(f"{CHROMA_DIR} exists; refusing to overwrite")
    chunk_ids = [c["chunk_id"] for c in read_jsonl(config.CHUNKS_PATH)]
    ordinal = np.zeros(len(wc), dtype=np.int64)
    for i in range(1, len(wc)):
        ordinal[i] = ordinal[i - 1] + 1 if wc[i] == wc[i - 1] else 0
    t = time.perf_counter()
    client = chromadb.PersistentClient(path=CHROMA_DIR, settings=Settings(anonymized_telemetry=False))
    col = client.create_collection(CHROMA_COLLECTION, configuration={"hnsw": {"space": "cosine"}}, embedding_function=None,
                                   metadata={"vectors_sha256": meta["vectors_sha256"], "chunk_set_hash": EXPECTED_CHUNK_SET_HASH,
                                             "n_windows": int(len(V))})
    for s in range(0, len(V), BATCH):
        e = min(s + BATCH, len(V))
        col.add(ids=[f"w{i:05d}" for i in range(s, e)], embeddings=V[s:e],
                metadatas=[{"chunk_id": chunk_ids[wc[i]], "chunk_index": int(wc[i]), "window_ordinal": int(ordinal[i])} for i in range(s, e)])
    t_add = time.perf_counter() - t
    col.query(query_embeddings=[V[0].tolist()], n_results=1, include=["distances"])  # forces the index to be built / loaded
    t_total = time.perf_counter() - t
    meta.update(library="chromadb", version=chromadb.__version__, collection=CHROMA_COLLECTION, count=col.count(),
                configuration=col.configuration, add_seconds=round(t_add, 3), add_and_first_query_seconds=round(t_total, 3),
                batch=BATCH, path=os.path.relpath(CHROMA_DIR, OUT))
    del col, client
    meta["size_bytes"] = dir_size(CHROMA_DIR)
    dump(os.path.join(OUT, "chroma_build.json"), meta)
    return meta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=("faiss", "chroma"), required=True)
    a = ap.parse_args()
    files = verify_embedding_files()
    V = np.ascontiguousarray(np.load(VECTORS), dtype=np.float32)
    wc = np.load(WINDOW_CHUNK)
    proc = psutil.Process()
    rss0 = proc.memory_info().rss
    meta = {"generated_at": time.strftime("%Y-%m-%d %H:%M:%S"), "python": sys.version.split()[0], "platform": platform.platform(),
            "vectors_sha256": files["window_vectors.npy"], "window_chunk_sha256": files["window_chunk.npy"],
            "n_windows": int(len(V)), "dim": int(V.shape[1]), "source": "existing production embeddings, no re-embedding"}
    meta = build_faiss(V, meta) if a.backend == "faiss" else build_chroma(V, wc, meta)
    mi = proc.memory_info()
    meta["rss_delta_mb"] = round((mi.rss - rss0) / 2**20, 1)
    meta["peak_working_set_mb"] = round(getattr(mi, "peak_wset", 0) / 2**20, 1)
    dump(FAISS_PATH + ".meta.json" if a.backend == "faiss" else os.path.join(OUT, "chroma_build.json"), meta)
    print({k: v for k, v in meta.items() if k not in ("configuration",)})


if __name__ == "__main__":
    main()
