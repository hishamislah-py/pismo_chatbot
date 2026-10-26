"""Retrieval metrics over a ranked chunk list and a question's valid gold labels.

* label recall@k: share of valid labels with at least one satisfying chunk in the top k (prior experiment's Recall@k)
* MRR: 1 / rank of the first chunk satisfying any label (0 when none in the evaluated depth)
* nDCG@k: label-level gain - a chunk earns 1 for each label it newly covers; IDCG places one new label per rank
* all-labels@k: every valid label covered in the top k (multi-source completeness; prior AllSources@k)
* KU recall@k: share of labels whose relevant KUs include one of the top-k distinct KUs of the ranking
"""
import math

DEPTH = 100


def label_hits(ranked_ids, label_sets, depth=DEPTH):
    """For each rank (1-based) the set of label indices satisfied by that chunk."""
    out = []
    for cid in ranked_ids[:depth]:
        out.append({j for j, s in enumerate(label_sets) if cid in s})
    return out


def first_relevant_rank(hits):
    for r, h in enumerate(hits, 1):
        if h:
            return r
    return None


def label_recall_at(hits, n_labels, k):
    if not n_labels:
        return None
    covered = set().union(*hits[:k]) if hits[:k] else set()
    return len(covered) / n_labels


def all_labels_at(hits, n_labels, k):
    if not n_labels:
        return None
    covered = set().union(*hits[:k]) if hits[:k] else set()
    return len(covered) == n_labels


def ndcg_at(hits, n_labels, k):
    if not n_labels:
        return None
    seen, dcg = set(), 0.0
    for r, h in enumerate(hits[:k], 1):
        new = h - seen
        if new:
            dcg += len(new) / math.log2(r + 1)
            seen |= new
    idcg = sum(1 / math.log2(r + 1) for r in range(1, min(n_labels, k) + 1))
    return dcg / idcg if idcg else 0.0


def mrr(hits):
    r = first_relevant_rank(hits)
    return 1.0 / r if r else 0.0


def ku_ranking(ranked_ids, chunk_ku):
    out, seen = [], set()
    for cid in ranked_ids:
        k = chunk_ku[cid]
        if k not in seen:
            seen.add(k)
            out.append(k)
    return out


def ku_recall_at(ku_rank, label_ku_sets, k):
    if not label_ku_sets:
        return None
    top = set(ku_rank[:k])
    return sum(1 for s in label_ku_sets if s & top) / len(label_ku_sets)


def evaluate(ranked_ids, label_sets, label_ku_sets, chunk_ku):
    hits = label_hits(ranked_ids, label_sets)
    n = len(label_sets)
    kr = ku_ranking(ranked_ids[:DEPTH], chunk_ku)
    return {
        "first_relevant_rank": first_relevant_rank(hits),
        "recall@5": label_recall_at(hits, n, 5), "recall@10": label_recall_at(hits, n, 10),
        "mrr": mrr(hits), "ndcg@5": ndcg_at(hits, n, 5), "ndcg@10": ndcg_at(hits, n, 10),
        "hit@5": bool(first_relevant_rank(hits) and first_relevant_rank(hits) <= 5),
        "hit@10": bool(first_relevant_rank(hits) and first_relevant_rank(hits) <= 10),
        "all_labels@5": all_labels_at(hits, n, 5), "all_labels@10": all_labels_at(hits, n, 10),
        "ku_recall@5": ku_recall_at(kr, label_ku_sets, 5), "ku_recall@10": ku_recall_at(kr, label_ku_sets, 10),
        "labels_covered@10": sorted(set().union(*hits[:10])) if hits[:10] else [],
    }


def mean(xs):
    xs = [x for x in xs if x is not None]
    return round(sum(xs) / len(xs), 4) if xs else None
