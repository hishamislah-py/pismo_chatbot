"""Step 1: verify and freeze the KU-only retrieval corpus, then chunk it.

Writes CORPUS_MANIFEST.csv, results/chunks.jsonl and results/corpus_summary.json. Exit 1 on any isolation failure.
Usage: python -B -E -s scripts/build_corpus.py
"""
import csv
import os
import statistics
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import EXP, MIG, RESULTS, dump_json, load_json, sha_bytes, write_jsonl  # noqa: E402
from corpus import MAX_CHARS, IsolationError, chunk_ku, load_corpus  # noqa: E402


def manifest_hash(kus):
    return sha_bytes("".join(f"{k['path']}\t{k['sha256']}\n" for k in sorted(kus, key=lambda k: k["path"])).encode())


def chunk_set_hash(chunks):
    return sha_bytes("".join(f"{c['chunk_id']}\t{c['sha256']}\n" for c in chunks).encode())


def main():
    try:
        kus, iso = load_corpus()
    except IsolationError as e:
        print("ISOLATION FAILURE:", e)
        sys.exit(1)
    kus.sort(key=lambda k: k["path"])
    chunks = []
    for ku in kus:
        chunks.extend(chunk_ku(ku))
    ids = Counter(c["chunk_id"] for c in chunks)
    dup = [i for i, n in ids.items() if n > 1]
    if dup:
        print("DUPLICATE CHUNK IDS:", dup[:10])
        sys.exit(1)
    for c in chunks:
        if not c["ku_path"].startswith("knowledge_units/") or not c["ku_path"].endswith(".md"):
            print("ISOLATION FAILURE: chunk from non-KU path", c["ku_path"])
            sys.exit(1)
    per_ku = Counter(c["ku_id"] for c in chunks)
    maxc = {}
    for c in chunks:
        maxc[c["ku_id"]] = max(maxc.get(c["ku_id"], 0), c["chars"])
    with open(os.path.join(EXP, "CORPUS_MANIFEST.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["ku_id", "ku_path", "category", "ku_type", "lifecycle", "bytes", "sha256", "n_sources", "chunks", "max_chunk_chars"])
        for k in kus:
            w.writerow([k["ku_id"], k["path"], k["category"], k["ku_type"], k["lifecycle"], k["bytes"], k["sha256"],
                        len(k["sources"]), per_ku[k["ku_id"]], maxc.get(k["ku_id"], 0)])
    write_jsonl(os.path.join(RESULTS, "chunks.jsonl"), chunks)
    sizes = sorted(c["chars"] for c in chunks)
    q = lambda p: sizes[min(len(sizes) - 1, int(p * len(sizes)))]
    mig_index = load_json(os.path.join(MIG, "work", "ku_index.json"))
    big = sorted(((k["bytes"], k["ku_id"]) for k in kus if k["bytes"] > 100_000), reverse=True)
    summary = {
        "ku_files_approved": len(kus), "unique_ku_ids": iso["unique_ku_ids"], "unique_content_hashes": iso["unique_content_hashes"],
        "rejected_files": iso["rejected"], "migration_ku_index_entries": len(mig_index),
        "ku_ids_match_migration_index": sorted(mig_index) == sorted(k["ku_id"] for k in kus),
        "corpus_manifest_hash": manifest_hash(kus), "chunk_count": len(chunks), "chunk_set_hash": chunk_set_hash(chunks),
        "chunking": {"max_body_chars": MAX_CHARS, "unit": "heading section; API operation kept whole when it fits; tables split by rows with header repeated; code fences reopened",
                     "index_text": "KU title + heading path + body (identical for every method)"},
        "chunk_chars": {"min": sizes[0], "p10": q(0.10), "median": statistics.median(sizes), "p90": q(0.90), "max": sizes[-1],
                        "mean": round(statistics.mean(sizes), 1)},
        "chunks_by_ku_type": dict(Counter(c["ku_type"] for c in chunks)),
        "chunks_by_category": dict(Counter(c["category"] for c in chunks)),
        "chunks_split_parts": sum(1 for c in chunks if c["parts"] > 1),
        "chunk_flags": dict(Counter(f for c in chunks for f in c["flags"])),
        "kus_over_100KB": [{"ku_id": i, "bytes": b, "chunks": per_ku[i]} for b, i in big],
        "kus_by_type": dict(Counter(k["ku_type"] for k in kus)), "kus_by_category": dict(Counter(k["category"] for k in kus)),
    }
    dump_json(os.path.join(RESULTS, "corpus_summary.json"), summary)
    for k in ("ku_files_approved", "unique_ku_ids", "unique_content_hashes", "rejected_files", "ku_ids_match_migration_index",
              "corpus_manifest_hash", "chunk_count", "chunk_set_hash", "chunk_chars", "chunks_split_parts"):
        print(f"{k}: {summary[k]}")


if __name__ == "__main__":
    main()
