"""Retrieval methods over one shared chunk list: BM25, exact-identifier lookup (separate enhancement), dense semantic
retrieval (sentence-transformers MiniLM), and weighted reciprocal rank fusion. All rankings are deterministic.
"""
import math
import os
import re
from collections import Counter, defaultdict

import numpy as np

STOP = set("a an the of to in for on and or is are be do does i my we our how what which when why can should with from "
           "that this it as by at into was were me you your there their them if then than so not no".split())
TOKEN_RX = re.compile(r"[a-z0-9]+")
COMPOUND_RX = re.compile(r"[a-z0-9]+(?:[-_/.:][a-z0-9]+)+")


def tokenize(text):
    """Lower-cased word tokens plus whole compound identifiers (operation ids, paths, headers, field and event names),
    so `x-account-id`, `encrypted_pan`, `v1/migrations/cards-pci` and `post-transfers-cancel` survive as single tokens."""
    s = text.lower()
    return [t for t in TOKEN_RX.findall(s) + COMPOUND_RX.findall(s) if t not in STOP]


class BM25:
    """Okapi BM25 with k1=1.5, b=0.75 and the non-negative idf ln(1 + (N - df + 0.5) / (df + 0.5))."""

    def __init__(self, texts, k1=1.5, b=0.75):
        self.k1, self.b = k1, b
        self.N = len(texts)
        self.postings = defaultdict(list)
        self.dl = np.zeros(self.N)
        for i, t in enumerate(texts):
            tf = Counter(tokenize(t))
            self.dl[i] = sum(tf.values())
            for term, f in tf.items():
                self.postings[term].append((i, f))
        self.avgdl = float(self.dl.mean()) if self.N else 0.0
        self.idf = {t: math.log(1 + (self.N - len(p) + 0.5) / (len(p) + 0.5)) for t, p in self.postings.items()}

    def scores(self, query):
        sc = np.zeros(self.N)
        for term in tokenize(query):
            p = self.postings.get(term)
            if not p:
                continue
            idx = np.fromiter((i for i, _ in p), dtype=np.int64, count=len(p))
            f = np.fromiter((x for _, x in p), dtype=np.float64, count=len(p))
            norm = self.k1 * (1 - self.b + self.b * self.dl[idx] / self.avgdl)
            sc[idx] += self.idf[term] * f * (self.k1 + 1) / (f + norm)
        return sc


def rank_by_score(scores, ids, positive_only=False):
    """Indices sorted by score desc, ties broken by chunk id asc. positive_only drops zero-score items."""
    order = sorted(range(len(ids)), key=lambda i: (-scores[i], ids[i]))
    if positive_only:
        order = [i for i in order if scores[i] > 0]
    return order


# ---------------------------------------------------------------- exact identifier lookup (optional enhancement)
ID_PATTERNS = [
    ("error_code", re.compile(r"\b[A-Z][A-Z0-9]{1,9}[0-9]{3,6}\b")),
    ("path", re.compile(r"(?<![\w/])/[A-Za-z0-9{}_\-.]+(?:/[A-Za-z0-9{}_\-.]+)+")),
    ("header", re.compile(r"\bx-[a-z0-9]+(?:-[a-z0-9]+)*\b", re.I)),
    ("hyphen_identifier", re.compile(r"\b[a-z0-9]+(?:-[a-z0-9]+){2,}\b")),
    ("snake_identifier", re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b")),
    ("camel_identifier", re.compile(r"\b[a-z]+[A-Z][A-Za-z0-9]*[a-z0-9][A-Za-z0-9]*\b")),
]
NOT_IDENTIFIERS = {"mTLS", "eCommerce", "iOS", "macOS"}  # lesson from the prior experiment: mTLS is not an identifier


def detect_identifiers(query):
    found = []
    for kind, rx in ID_PATTERNS:
        for m in rx.findall(query):
            if m in NOT_IDENTIFIERS or m in found:
                continue
            if kind == "camel_identifier" and m[1:].isupper():
                continue
            found.append(m)
    # keep the longest identifiers only (a path already contains its hyphenated segment)
    return [f for f in found if not any(f != g and f in g for g in found)]


def exact_rerank(base_order, texts_lower, identifiers):
    """Stable promotion: chunks containing every identifier, then chunks containing any, each in base order; then the rest."""
    if not identifiers:
        return list(base_order), 0
    idl = [i.lower() for i in identifiers]
    all_hit, any_hit, rest = [], [], []
    for i in base_order:
        t = texts_lower[i]
        n = sum(1 for x in idl if x in t)
        (all_hit if n == len(idl) else any_hit if n else rest).append(i)
    return all_hit + any_hit + rest, len(all_hit) + len(any_hit)


def exact_candidates(texts_lower, identifiers):
    idl = [i.lower() for i in identifiers]
    return [i for i, t in enumerate(texts_lower) if any(x in t for x in idl)]


# ---------------------------------------------------------------- reciprocal rank fusion
RRF_K = 60


def rrf(rankings, weights, ids, k=RRF_K, depth=None):
    """score(d) = sum_m w_m / (k + rank_m(d)), rank 1-based; a method contributes only for items in its list.
    Ties: higher fused score, then better best single-method rank, then better first-method rank, then chunk id."""
    score = defaultdict(float)
    best = {}
    first = {}
    for m, (order, w) in enumerate(zip(rankings, weights)):
        lim = order if depth is None else order[:depth]
        for r, i in enumerate(lim, 1):
            score[i] += w / (k + r)
            best[i] = min(best.get(i, r), r)
            if m == 0:
                first[i] = r
    big = 10 ** 9
    return sorted(score, key=lambda i: (-round(score[i], 12), best[i], first.get(i, big), ids[i]))


# ---------------------------------------------------------------- dense semantic retrieval
WINDOW_CHARS = 1000
WINDOW_STRIDE = 800


def windows_for(header, body):
    """Character windows over the chunk body, each prefixed with the chunk's context header. MiniLM reads at most 256
    word pieces, so long chunks are covered by several windows and scored by their best window (max-sim)."""
    if len(body) <= WINDOW_CHARS:
        return [header + body]
    out, start = [], 0
    while start < len(body):
        out.append(header + body[start:start + WINDOW_CHARS])
        if start + WINDOW_CHARS >= len(body):
            break
        start += WINDOW_STRIDE
    return out


def load_embedder():
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    from sentence_transformers import SentenceTransformer
    from common import HF_SNAPSHOT
    return SentenceTransformer(HF_SNAPSHOT, device="cpu")


class Dense:
    def __init__(self, window_vecs, window_chunk, n_chunks):
        self.V = window_vecs.astype(np.float32)
        self.wc = window_chunk
        self.n = n_chunks

    def scores(self, qvec):
        s = self.V @ qvec.astype(np.float32)
        out = np.full(self.n, -1.0, dtype=np.float64)
        np.maximum.at(out, self.wc, s)
        return out
