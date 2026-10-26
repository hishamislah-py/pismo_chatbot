"""Step 2: load the frozen prior benchmark (read from the original zip), map and verify every gold label against the
source corpus and the KU chunks, add the separately identified extension set, and freeze BENCHMARK.json.

Label verification is independent of retrieval: it only reads source files, KU chunks and labels.
Usage: python -B -E -s scripts/build_benchmark.py
"""
import os
import re
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (EXP, PRIOR_BENCH_MEMBER, PRIOR_BENCH_SHA, PRIOR_ZIP, PRIOR_ZIP_SHA, RESULTS, SOURCE_CORPUS,  # noqa: E402
                    dump_json, load_json, read_jsonl, sha_bytes, sha_file, sha_json)
from labels import chunk_satisfies, label_key  # noqa: E402

WORKFLOW = {"A": "Endpoint discovery", "B": "Request and response fields", "C": "Errors and troubleshooting",
            "D": "Events and webhooks", "E": "Lifecycle and changelog", "F": "Cross-KU workflows", "G": "Missing or ambiguous"}
# Evaluation annotations added to primary questions. They do not change any question text or gold label; they record
# lifecycle sensitivity, the migration issue a question exercises, and the misleading near-matches named in the
# prior benchmark's own notes, so unanswerable/lifecycle behaviour can be measured.
PRIMARY_ANNOTATIONS = {
    "B3": {"lifecycle_sensitive": True}, "B4": {"lifecycle_sensitive": True}, "B5": {"lifecycle_sensitive": True},
    "C3": {"lifecycle_sensitive": True},
    "D6": {"migration_issue": "SG-01", "required_statement": {"event": "account-status-change-2", "match": "not documented in the available source corpus"}},
    "E1": {"lifecycle_sensitive": True, "migration_issue": "SC-02"}, "E2": {"lifecycle_sensitive": True, "migration_issue": "SG-02"},
    "E3": {"lifecycle_sensitive": True}, "E4": {"lifecycle_sensitive": True}, "E5": {"lifecycle_sensitive": True},
    "E6": {"lifecycle_sensitive": True}, "E7": {"lifecycle_sensitive": True},
    "G1": {"distractors": ["99\\.999"]},
    "G3": {"migration_issue": "SG-03", "absent_identifier": "cards-pci/go-live", "distractors": ["go-live|golive"]},
    "G4": {"distractors": ["Ordering dimensions"]},
    "G5": {"lifecycle_sensitive": True, "migration_issue": "SC-01"},
    "G7": {"absent_identifier": "MIGR-0400", "distractors": ["MIGR0000[12]"]},
}


def source_text(path_or_dir):
    """Concatenated text of a source file, or of every file under a folder label."""
    full = os.path.join(SOURCE_CORPUS, path_or_dir)
    if path_or_dir.endswith("/"):
        out = []
        for root, _, files in os.walk(full):
            for f in files:
                out.append(open(os.path.join(root, f), encoding="utf-8", errors="replace").read())
        return "\n".join(out) if out else None
    if not os.path.isfile(full):
        return None
    return open(full, encoding="utf-8", errors="replace").read()


def verify_label(label, chunks, ku_text):
    out = {"label": label, "key": label_key(label)}
    if "ku" in label:
        t = ku_text.get(label["ku"])
        out["source_evidence"] = "n/a (KU-generated content)" if t is not None else "ku_missing"
        src_ok = t is not None and (not label.get("match") or re.search(label["match"], t, re.I) is not None)
    else:
        t = source_text(label["file"])
        if t is None:
            out["source_evidence"] = "source_file_missing"
            src_ok = False
        else:
            src_ok = not label.get("match") or re.search(label["match"], t, re.I) is not None
            out["source_evidence"] = "regex_found_in_source" if label.get("match") and src_ok else (
                "file_present" if src_ok else "regex_absent_from_source")
    hits = [c for c in chunks if chunk_satisfies(c, label)]
    out["relevant_chunk_ids"] = [c["chunk_id"] for c in hits]
    out["relevant_ku_ids"] = sorted({c["ku_id"] for c in hits})
    out["evidence_sections"] = sorted({" > ".join(c["heading_path"][1:]) or "(intro)" for c in hits})[:25]
    if not src_ok:
        out["status"] = "invalid_label"
    elif not hits:
        kus_with_file = [k for k, v in ku_files.items() if any(s == label.get("file") or (label.get("file", "").endswith("/") and s.startswith(label["file"])) for s in v)]
        whole = any(re.search(label["match"], ku_text[k], re.I) for k in kus_with_file) if label.get("match") else bool(kus_with_file)
        out["status"] = "chunking_split" if whole else "ku_coverage_gap"
    else:
        out["status"] = "valid"
    out["broad"] = len(hits) > 40
    return out


def required_statement_check(req, chunks, ku_text):
    if "ku" in req:
        targets = [req["ku"]]
    else:  # event: the event-catalogue KU(s) whose table lists the event
        targets = sorted({c["ku_id"] for c in chunks if c["ku_type"] == "event_catalogue" and f"`{req['event']}`" in c["text"]})
    ok = bool(targets) and all(t in ku_text and re.search(re.escape(req["match"]), ku_text[t], re.I) for t in targets)
    return {"targets": targets, "match": req["match"], "present": ok}


def build_question(q, chunks, ku_text, set_name):
    labels = [verify_label(l, chunks, ku_text) for l in q.get("expected", [])]
    out = {k: v for k, v in q.items() if k != "expected"}
    out["set"] = set_name
    out["workflow"] = WORKFLOW.get(q["cat"][0], q["cat"]) if set_name == "primary" else q["cat"]
    out["labels"] = labels
    out["scored_labels"] = [l["key"] for l in labels if l["status"] == "valid"]
    out["relevant_ku_ids"] = sorted({k for l in labels if l["status"] == "valid" for k in l["relevant_ku_ids"]})
    out["multi_ku"] = len([l for l in labels if l["status"] == "valid"]) > 1
    if q.get("answerability") == "none":
        out["scored"] = False
    else:
        out["scored"] = bool(out["scored_labels"])
    if q.get("absent_identifier"):
        hits = [k for k, t in ku_text.items() if q["absent_identifier"].lower() in t.lower()]
        out["absent_identifier_check"] = {"identifier": q["absent_identifier"], "kus_containing": hits, "absent": not hits}
    if q.get("required_statement"):
        out["required_statement_check"] = required_statement_check(q["required_statement"], chunks, ku_text)
    return out


def main():
    global ku_files
    if sha_file(PRIOR_ZIP) != PRIOR_ZIP_SHA:
        print("prior experiment zip hash mismatch")
        sys.exit(1)
    raw = zipfile.ZipFile(PRIOR_ZIP).read(PRIOR_BENCH_MEMBER)
    if sha_bytes(raw) != PRIOR_BENCH_SHA:
        print("frozen prior benchmark hash mismatch")
        sys.exit(1)
    import json
    prior = json.loads(raw)
    ext_path = os.path.join(EXP, "benchmark_inputs", "extension_questions_v1.json")
    ext = load_json(ext_path)
    chunks = read_jsonl(os.path.join(RESULTS, "chunks.jsonl"))
    summary = load_json(os.path.join(RESULTS, "corpus_summary.json"))
    ku_text, ku_files = {}, {}
    for c in chunks:
        ku_text[c["ku_id"]] = ku_text.get(c["ku_id"], "") + "\n" + c["text"]
        ku_files[c["ku_id"]] = c["ku_sources"]
    primary = []
    for q in prior["questions"]:
        q2 = dict(q)
        q2.update(PRIMARY_ANNOTATIONS.get(q["id"], {}))
        primary.append(build_question(q2, chunks, ku_text, "primary"))
    extension = [build_question(q, chunks, ku_text, "extension") for q in ext["questions"]]
    ids = [q["id"] for q in primary + extension]
    assert len(ids) == len(set(ids)), "duplicate question ids"
    bench = {
        "_meta": {
            "primary_source": {"zip": os.path.basename(PRIOR_ZIP), "zip_sha256": PRIOR_ZIP_SHA, "member": PRIOR_BENCH_MEMBER,
                               "member_sha256": PRIOR_BENCH_SHA, "prior_meta": prior["_meta"]},
            "extension_source": {"file": "benchmark_inputs/extension_questions_v1.json", "sha256": sha_file(ext_path), "meta": ext["_meta"]},
            "corpus_manifest_hash": summary["corpus_manifest_hash"], "chunk_set_hash": summary["chunk_set_hash"],
            "label_semantics": "scripts/labels.py", "primary_annotations": PRIMARY_ANNOTATIONS,
            "statuses": {"valid": "source evidence found and at least one KU chunk satisfies the label (scored)",
                         "ku_coverage_gap": "evidence exists in the source but no KU chunk carries it (not scored; KU issue)",
                         "chunking_split": "the KU text matches but no single chunk does (not scored; chunking issue)",
                         "invalid_label": "the label's regex/file is not found in the source corpus (not scored; label issue)"},
        },
        "primary": primary, "extension": extension,
    }
    content_hash = sha_json({"primary": primary, "extension": extension})
    bench["_meta"]["benchmark_content_sha256"] = content_hash
    dump_json(os.path.join(EXP, "BENCHMARK.json"), bench)
    with open(os.path.join(EXP, "BENCHMARK.sha256"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(f"{content_hash}  BENCHMARK.json (content: primary+extension, canonical JSON)\n")
    from collections import Counter
    for name, qs in (("primary", primary), ("extension", extension)):
        st = Counter(l["status"] for q in qs for l in q["labels"])
        print(f"{name}: {len(qs)} questions, scored {sum(q['scored'] for q in qs)}, label statuses {dict(st)}")
        for q in qs:
            bad = [f"{l['key']} -> {l['status']} ({l['source_evidence']})" for l in q["labels"] if l["status"] != "valid"]
            broad = [l["key"] for l in q["labels"] if l["broad"]]
            extra = []
            if "absent_identifier_check" in q:
                extra.append(f"absent={q['absent_identifier_check']['absent']}")
            if "required_statement_check" in q:
                extra.append(f"statement={q['required_statement_check']['present']} {q['required_statement_check']['targets']}")
            if bad or broad or extra:
                print(f"  {q['id']}: {bad} broad={broad} {' '.join(extra)}")
    print("benchmark content sha256:", content_hash)


if __name__ == "__main__":
    main()
