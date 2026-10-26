"""Step 3b: sanity checks for the dense embedder on Pismo-specific inputs. Criteria are fixed in advance; a failed check
is a finding about the model, not an error to hide. Writes results/semantic_sanity.json.
Usage: python -B -s scripts/semantic_sanity.py
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RESULTS, dump_json, load_json, read_jsonl  # noqa: E402
from retrievers import Dense, load_embedder, rank_by_score  # noqa: E402

RANK_CHECKS = [  # id, kind, query, acceptable KU ids, criterion: an acceptable KU's chunk within top N
    ("S1", "exact operationId", "post-payments-v1-hold-funds-unblock", ["KU-API-core-platform-payment-methods--hold-funds", "KU-PAY-hold-funds"], 10),
    ("S2", "error code", "WEAM0001", ["KU-ERR-codes-weam"], 10),
    ("S3", "field name", "encrypted_pan", ["KU-API-migrations--card-migration", "KU-CHG-2-october-2026"], 10),
    ("S4", "paraphrase (source says 'transfer')", "move money from one customer account to another account",
     ["KU-PAY-transfers-make-and-cancel", "KU-API-core-platform-payment-methods--payment-methods-part-02",
      "KU-API-core-platform-payment-methods--payment-methods-part-03", "KU-PAY-single-ledger-entries-and-book-transfers"], 10),
    ("S5", "paraphrase (source says 'hold funds' / 'court order')", "freeze part of a balance so the customer cannot spend it because a judge ordered it",
     ["KU-PAY-hold-funds", "KU-CORE-legal-blocks", "KU-API-core-platform-payment-methods--hold-funds"], 10),
]
PAIR_CHECKS = [  # id, query, text expected closer, text expected further (confusable concepts)
    ("P1", "set money aside until a scheduled release date and then pay it out automatically",
     "An account holder can create an earmark to schedule a cash-out, holding needed funds in reserve until a scheduled date and time.",
     "Use the hold funds endpoint to block an amount in an account, for example because of a court order."),
    ("P2", "make migrated PCI cards go live",
     "Migrate PCI cards: POST /v1/migrations/cards-pci migrates card data including the PAN or encrypted_pan.",
     "Accounts go-live: sets the migration status of each account to MIGRATED."),
    ("P3", "verify that a webhook request was sent by Pismo",
     "Verifying webhook requests: validate the signature header of each webhook call with your secret.",
     "Rate limiting sets the maximum number of simultaneous requests allowed through an API."),
]


def main():
    chunks = read_jsonl(os.path.join(RESULTS, "chunks.jsonl"))
    ids = [c["chunk_id"] for c in chunks]
    emb = os.path.join(RESULTS, "embeddings")
    dense = Dense(np.load(os.path.join(emb, "window_vectors.npy")), np.load(os.path.join(emb, "window_chunk.npy")), len(chunks))
    model = load_embedder()
    out = {"model": load_json(os.path.join(emb, "embedding_meta.json"))["model"], "rank_checks": [], "pair_checks": [], "self_similarity": None}
    v = model.encode(["Hold funds on an account"] * 2, normalize_embeddings=True)
    out["self_similarity"] = {"cosine": round(float(v[0] @ v[1]), 6), "pass": float(v[0] @ v[1]) >= 0.999}
    for sid, kind, q, ok, n in RANK_CHECKS:
        qv = model.encode([q], normalize_embeddings=True)[0]
        order = rank_by_score(dense.scores(qv), ids)
        kus = [chunks[i]["ku_id"] for i in order]
        first = next((r for r, k in enumerate(kus, 1) if k in ok), None)
        out["rank_checks"].append({"id": sid, "kind": kind, "query": q, "acceptable_kus": ok, "criterion": f"acceptable KU chunk within top {n}",
                                   "first_acceptable_rank": first, "pass": bool(first and first <= n), "top5_kus": kus[:5]})
    for pid, q, near, far in PAIR_CHECKS:
        e = model.encode([q, near, far], normalize_embeddings=True)
        a, b = float(e[0] @ e[1]), float(e[0] @ e[2])
        out["pair_checks"].append({"id": pid, "query": q, "sim_expected_closer": round(a, 4), "sim_expected_further": round(b, 4), "pass": a > b})
    dump_json(os.path.join(RESULTS, "semantic_sanity.json"), out)
    print("self-similarity", out["self_similarity"])
    for r in out["rank_checks"]:
        print(f"{r['id']} {'PASS' if r['pass'] else 'FAIL'} {r['kind']:40} first acceptable rank {r['first_acceptable_rank']}  top5 {r['top5_kus'][:3]}")
    for r in out["pair_checks"]:
        print(f"{r['id']} {'PASS' if r['pass'] else 'FAIL'} closer {r['sim_expected_closer']} vs further {r['sim_expected_further']}")


if __name__ == "__main__":
    main()
