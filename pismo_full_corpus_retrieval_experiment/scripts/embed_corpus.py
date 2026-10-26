"""Step 3: embed every chunk (window max-sim) with the local, offline MiniLM model. No network, no paid API.

Writes results/embeddings/{window_vectors.npy, window_chunk.npy, embedding_meta.json}. Re-uses the cache when the
chunk set, model revision and window settings are unchanged.
Usage: python -B -E -s scripts/embed_corpus.py
"""
import os
import platform
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import EMBED_MODEL, EMBED_REVISION, HF_SNAPSHOT, RESULTS, dump_json, load_json, read_jsonl, sha_file  # noqa: E402
from corpus import index_text  # noqa: E402
from retrievers import WINDOW_CHARS, WINDOW_STRIDE, load_embedder, windows_for  # noqa: E402

OUT = os.path.join(RESULTS, "embeddings")


def main():
    summary = load_json(os.path.join(RESULTS, "corpus_summary.json"))
    meta_path = os.path.join(OUT, "embedding_meta.json")
    if os.path.exists(meta_path):
        m = load_json(meta_path)
        if m.get("chunk_set_hash") == summary["chunk_set_hash"] and m.get("revision") == EMBED_REVISION and \
                m.get("window_chars") == WINDOW_CHARS and m.get("window_stride") == WINDOW_STRIDE:
            print("embedding cache is current:", m["n_windows"], "windows")
            return
    chunks = read_jsonl(os.path.join(RESULTS, "chunks.jsonl"))
    texts, owner = [], []
    for i, c in enumerate(chunks):
        full = index_text(c)
        header = full[: len(full) - len(c["text"])]
        for w in windows_for(header, c["text"]):
            texts.append(w)
            owner.append(i)
    t0 = time.time()
    model = load_embedder()
    import sentence_transformers
    import torch
    t1 = time.time()
    vecs = model.encode(texts, batch_size=64, normalize_embeddings=True, show_progress_bar=False, convert_to_numpy=True)
    t2 = time.time()
    os.makedirs(OUT, exist_ok=True)
    np.save(os.path.join(OUT, "window_vectors.npy"), vecs.astype(np.float32))
    np.save(os.path.join(OUT, "window_chunk.npy"), np.array(owner, dtype=np.int64))
    meta = {
        "model": EMBED_MODEL, "revision": EMBED_REVISION, "local_snapshot": HF_SNAPSHOT,
        "model_safetensors_sha256": sha_file(os.path.join(HF_SNAPSHOT, "model.safetensors")),
        "dimension": int(model.get_sentence_embedding_dimension()), "max_seq_length_tokens": int(model.max_seq_length),
        "similarity": "cosine (L2-normalised vectors, dot product); chunk score = max over its windows",
        "query_encoding": "raw question text, no instruction prefix",
        "window_chars": WINDOW_CHARS, "window_stride": WINDOW_STRIDE, "window_text": "KU title + heading path header + body window",
        "n_chunks": len(chunks), "n_windows": len(texts), "chunk_set_hash": summary["chunk_set_hash"],
        "truncated_windows_note": "windows longer than 256 word pieces are truncated by the model",
        "sentence_transformers": sentence_transformers.__version__, "torch": torch.__version__,
        "python": platform.python_version(), "device": "cpu", "network": "HF_HUB_OFFLINE=1 (cached snapshot only)",
        "load_seconds": round(t1 - t0, 1), "encode_seconds": round(t2 - t1, 1),
    }
    dump_json(meta_path, meta)
    print({k: meta[k] for k in ("model", "revision", "dimension", "n_chunks", "n_windows", "load_seconds", "encode_seconds")})


if __name__ == "__main__":
    main()
