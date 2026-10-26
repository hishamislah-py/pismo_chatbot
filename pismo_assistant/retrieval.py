"""Retrieval: hybrid RRF (BM25 2:1 MiniLM) + exact-identifier promotion over the frozen KU chunk index.

Reuses the experiment's retrieval code unchanged (scripts/retrievers.py). At start-up it verifies that the index is
KU-only and still matches the approved knowledge units on disk.
"""
import json
import os
from dataclasses import dataclass, field

import numpy as np

from . import config

config.ensure_experiment_on_path()
from corpus import approved_ku_files, index_text, load_ku  # noqa: E402
from retrievers import BM25, Dense, detect_identifiers, exact_rerank, load_embedder, rank_by_score, rrf  # noqa: E402
from common import sha_bytes  # noqa: E402


class IndexIntegrityError(Exception):
    pass


@dataclass
class Hit:
    chunk: dict
    rank: int
    origin: str = "retrieved"  # retrieved | linked_operation | operation_events | lifecycle
    reason: str = ""
    extra: dict = field(default_factory=dict)

    @property
    def chunk_id(self):
        return self.chunk["chunk_id"]


def _read_chunks(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def verify_index(chunks, summary, embed_meta, check_ku_files=True):
    """Fail if the index contains non-KU material or no longer matches the approved KU files."""
    problems = []
    for c in chunks:
        if not (c.get("ku_path", "").startswith("knowledge_units/") and c["ku_path"].endswith(".md") and c.get("ku_id", "").startswith("KU-")):
            problems.append(f"non-KU chunk in index: {c.get('ku_path')}")
            break
    chunk_hash = sha_bytes("".join(f"{c['chunk_id']}\t{c['sha256']}\n" for c in chunks).encode())
    if chunk_hash != summary["chunk_set_hash"]:
        problems.append("chunks.jsonl does not match corpus_summary.json")
    if embed_meta["chunk_set_hash"] != chunk_hash:
        problems.append("embeddings were built for a different chunk set")
    if check_ku_files:
        approved, _ = approved_ku_files()
        rows = sorted((rel, load_ku(rel)["sha256"]) for rel in approved)
        if sha_bytes("".join(f"{p}\t{h}\n" for p, h in rows).encode()) != summary["corpus_manifest_hash"]:
            problems.append("knowledge_units/ changed since the index was built (corpus manifest hash differs)")
    if problems:
        raise IndexIntegrityError("; ".join(problems))
    return chunk_hash


class HybridRetriever:
    def __init__(self, chunks_path=config.CHUNKS_PATH, check_ku_files=True, embedder=None):
        self.chunks = _read_chunks(chunks_path)
        with open(config.CORPUS_SUMMARY_PATH, encoding="utf-8") as fh:
            summary = json.load(fh)
        with open(os.path.join(config.EMBEDDINGS_DIR, "embedding_meta.json"), encoding="utf-8") as fh:
            self.embed_meta = json.load(fh)
        self.chunk_set_hash = verify_index(self.chunks, summary, self.embed_meta, check_ku_files)
        self.ids = [c["chunk_id"] for c in self.chunks]
        self.by_id = {c["chunk_id"]: c for c in self.chunks}
        texts = [index_text(c) for c in self.chunks]
        self.texts_lower = [t.lower() for t in texts]
        self.bm25 = BM25(texts)
        self.dense = Dense(np.load(os.path.join(config.EMBEDDINGS_DIR, "window_vectors.npy")),
                           np.load(os.path.join(config.EMBEDDINGS_DIR, "window_chunk.npy")), len(self.chunks))
        self.embedder = embedder or load_embedder()

    def ranked(self, question):
        """Full ranking (chunk indices) and the number of exact-identifier matches promoted to the front."""
        if not question or not question.strip():
            return [], 0
        qv = self.embedder.encode([question], normalize_embeddings=True, convert_to_numpy=True)[0]
        b_order = rank_by_score(self.bm25.scores(question), self.ids, positive_only=True)
        d_order = rank_by_score(self.dense.scores(qv), self.ids)
        fused = rrf([b_order, d_order], list(config.RRF_WEIGHTS), self.ids)
        idents = detect_identifiers(question)
        return exact_rerank(fused, self.texts_lower, idents)

    def search(self, question, k=config.TOP_K):
        """Top-k chunks of the ranking; KU navigation sections are skipped when EXCLUDE_NAV_FROM_TOP_K is set.
        Hit.rank keeps the chunk's position in the full ranking."""
        order, n_exact = self.ranked(question)
        hits = []
        for r, i in enumerate(order, 1):
            if len(hits) >= k:
                break
            if config.EXCLUDE_NAV_FROM_TOP_K and is_navigation(self.chunks[i]):
                continue
            hits.append(Hit(self.chunks[i], r, "retrieved", "exact identifier match" if r <= n_exact else "hybrid rank"))
        return hits


def is_navigation(chunk):
    """KU navigation sections (no answer content): the KU header chunk and the sections listed in config.NAV_SECTIONS."""
    return chunk["section_heading"] in config.NAV_SECTIONS or chunk["chunk_id"].endswith("::intro")
