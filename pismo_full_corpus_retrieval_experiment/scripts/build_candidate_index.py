"""Build a CANDIDATE retrieval index from a versioned KU collection with the existing, unchanged steps
(build_corpus.main = chunking, embed_corpus.main = MiniLM window embeddings). Writes only under candidates/<name>/;
never touches results/ (the index the assistant serves) or the approved KU collection.

Usage: python -B -E -s scripts/build_candidate_index.py <ku_collection_dir> <name>
  e.g. python -B -E -s scripts/build_candidate_index.py ../pismo_knowledge_units_migration_v1_1 ku_v1_1
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    mig, name = os.path.abspath(argv[0]), argv[1]
    out = os.path.join(common.EXP, "candidates", name)
    if os.path.realpath(out) == os.path.realpath(common.RESULTS) or os.path.realpath(mig) == os.path.realpath(common.MIG):
        print("refusing: the candidate must use a versioned KU collection and its own output folder")
        return 2
    if not os.path.isfile(os.path.join(mig, "knowledge_units", ".generated_by_build_kus")):
        print(f"refusing: {mig} has no generated knowledge_units/ folder")
        return 2
    if os.path.exists(out) and os.listdir(out):
        print(f"refusing: {out} exists and is not empty")
        return 2
    os.makedirs(out)
    # the build modules bind these paths at import time, so set them before importing
    common.MIG, common.KU_DIR, common.RESULTS = mig, os.path.join(mig, "knowledge_units"), out
    import build_corpus
    import embed_corpus
    build_corpus.EXP = out  # CORPUS_MANIFEST.csv goes next to the candidate, not into the experiment root
    assert build_corpus.RESULTS == out and embed_corpus.OUT == os.path.join(out, "embeddings")
    t = time.time()
    build_corpus.main()
    embed_corpus.main()
    summary = common.load_json(os.path.join(out, "corpus_summary.json"))
    common.dump_json(os.path.join(out, "CANDIDATE.json"), {
        "status": "candidate - not served; the assistant reads results/ (pismo_assistant/config.py)",
        "ku_collection": os.path.relpath(mig, common.HANDOFF).replace(os.sep, "/"),
        "corpus_manifest_hash": summary["corpus_manifest_hash"], "chunk_set_hash": summary["chunk_set_hash"],
        "chunk_count": summary["chunk_count"], "built_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "build_seconds": round(time.time() - t, 1),
    })
    print("candidate index written to", out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
