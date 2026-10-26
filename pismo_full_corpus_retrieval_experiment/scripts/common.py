"""Shared paths, hashing and JSON helpers for the full-corpus retrieval experiment (read-only on every input)."""
import hashlib
import json
import os

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HANDOFF = os.path.dirname(EXP)
MIG = os.path.join(HANDOFF, "pismo_knowledge_units_migration")
KU_DIR = os.path.join(MIG, "knowledge_units")
SOURCE_CORPUS = os.path.join(HANDOFF, "pismo_kb_release_r2", "kb_corpus")  # used only to verify gold labels, never indexed
DOWNLOADS = os.path.dirname(HANDOFF)
PRIOR_ZIP = os.path.join(DOWNLOADS, "pismo_retrieval_experiment_v2.zip")
PRIOR_ZIP_SHA = "061801cd9d573aff025a200fcbf98cf44abc87a3f3f62b25d020aebfaad60f27"
PRIOR_BENCH_MEMBER = "pismo_retrieval_experiment_v2/benchmark/benchmark_questions_v2.json"
PRIOR_BENCH_SHA = "71a969f3d180f6f9f8156e335328eddf43eea3dc21bf5ee5bc975c2a994c04da"
PRIOR_CORPUS_ZIP = os.path.join(DOWNLOADS, "pismo_kb_r2_for_experiments.zip")
PRIOR_CORPUS_ZIP_SHA = "31f5b9292fe5324c955e13da33a84b0d293c5a64d7a48bc18d19f5901371389a"
RESULTS = os.path.join(EXP, "results")
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBED_REVISION = "1110a243fdf4706b3f48f1d95db1a4f5529b4d41"
HF_SNAPSHOT = os.path.join(os.path.expanduser("~"), ".cache", "huggingface", "hub",
                           "models--sentence-transformers--all-MiniLM-L6-v2", "snapshots", EMBED_REVISION)


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def canonical_json(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha_json(obj):
    return sha_bytes(canonical_json(obj).encode("utf-8"))


def dump_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def read_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]
