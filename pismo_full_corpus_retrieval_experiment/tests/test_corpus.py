"""Corpus isolation, duplicate ids, stable chunk ids, provenance and reproducible corpus hashes."""
import csv
import os

import pytest

import corpus
from common import EXP, MIG, sha_bytes
from conftest import make_ku


def _write(p, text):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def _ku_file(ku_id, cat):
    return f"---\nku_id: {ku_id}\ntitle: t\ncategory: {cat}\nku_type: workflow_guide\nlifecycle: current\nsources: []\n---\n# t\n"


def test_real_corpus_is_ku_only(summary, chunks):
    assert summary["ku_files_approved"] == 623
    assert summary["unique_ku_ids"] == 623
    assert summary["ku_ids_match_migration_index"] is True
    assert [r["path"] for r in summary["rejected_files"]] == ["knowledge_units/.generated_by_build_kus"]
    for c in chunks:
        assert c["ku_path"].startswith("knowledge_units/") and c["ku_path"].endswith(".md")
        assert c["ku_id"].startswith("KU-")
        assert "kb_corpus" not in c["ku_path"] and "MIGRATION_MANIFEST" not in c["ku_path"]


def test_isolation_rejects_non_ku_files(tmp_path, monkeypatch):
    root = tmp_path / "mig"
    kdir = root / "knowledge_units"
    _write(str(kdir / "cat" / "KU-A.md"), _ku_file("KU-A", "cat"))
    _write(str(kdir / "cat" / "notes.md"), "not a KU")
    _write(str(kdir / "cat" / "Migrations.yaml"), "openapi: 3")
    _write(str(kdir / "VALIDATION_REPORT.csv"), "x")
    monkeypatch.setattr(corpus, "KU_DIR", str(kdir))
    monkeypatch.setattr(corpus, "MIG", str(root))
    ok, rejected = corpus.approved_ku_files()
    assert ok == ["knowledge_units/cat/KU-A.md"]
    assert {r for r, _ in rejected} == {"knowledge_units/cat/notes.md", "knowledge_units/cat/Migrations.yaml", "knowledge_units/VALIDATION_REPORT.csv"}


def test_isolation_fails_on_ku_without_front_matter(tmp_path, monkeypatch):
    root = tmp_path / "mig"
    _write(str(root / "knowledge_units" / "cat" / "KU-B.md"), "# no front matter\n")
    monkeypatch.setattr(corpus, "KU_DIR", str(root / "knowledge_units"))
    monkeypatch.setattr(corpus, "MIG", str(root))
    with pytest.raises(corpus.IsolationError):
        corpus.load_corpus(check_source_copies=False)


def test_duplicate_ku_ids_fail(tmp_path, monkeypatch):
    root = tmp_path / "mig"
    _write(str(root / "knowledge_units" / "a" / "KU-DUP.md"), _ku_file("KU-DUP", "a"))
    _write(str(root / "knowledge_units" / "b" / "KU-DUP.md"), _ku_file("KU-DUP", "b"))
    monkeypatch.setattr(corpus, "KU_DIR", str(root / "knowledge_units"))
    monkeypatch.setattr(corpus, "MIG", str(root))
    with pytest.raises(corpus.IsolationError, match="duplicate KU id"):
        corpus.load_corpus(check_source_copies=False)


def test_chunk_ids_unique_and_stable(chunks):
    ids = [c["chunk_id"] for c in chunks]
    assert len(ids) == len(set(ids))
    ku = corpus.load_ku("knowledge_units/transfers_and_payments/KU-PAY-hold-funds.md")
    a = corpus.chunk_ku(ku)
    b = corpus.chunk_ku(corpus.load_ku("knowledge_units/transfers_and_payments/KU-PAY-hold-funds.md"))
    assert [c["chunk_id"] for c in a] == [c["chunk_id"] for c in b]
    stored = [c for c in chunks if c["ku_id"] == "KU-PAY-hold-funds"]
    assert [c["chunk_id"] for c in a] == [c["chunk_id"] for c in stored]
    assert [c["sha256"] for c in a] == [c["sha256"] for c in stored]


def test_chunk_ids_follow_identity_not_position():
    body = "# T\n\n## Alpha\n\ntext a\n\n## Beta\n\ntext b\n"
    ids1 = [c["chunk_id"] for c in corpus.chunk_ku(make_ku(body=body))]
    body2 = "# T\n\n## New first\n\nnew\n\n## Alpha\n\ntext a\n\n## Beta\n\ntext b\n"
    ids2 = [c["chunk_id"] for c in corpus.chunk_ku(make_ku(body=body2))]
    assert "KU-T-x::alpha" in ids1 and "KU-T-x::alpha" in ids2 and "KU-T-x::beta" in ids2


def test_provenance_preserved(chunks):
    for c in chunks:
        for k in ("chunk_id", "ku_id", "ku_title", "ku_path", "heading_path", "section_heading", "parent_heading", "lifecycle", "ku_type"):
            assert c[k] is not None
        assert c["source_refs"], c["chunk_id"]
        assert all(r["url"] and r["sha256"] for r in c["source_refs"]), c["chunk_id"]
        if c["source_path"]:
            assert c["source_path"] in c["ku_sources"]
            assert [r["path"] for r in c["source_refs"]] == [c["source_path"]]


def test_verbatim_markers_not_indexed_but_recorded(chunks):
    assert not any("<!-- source:begin" in c["text"] or "<!-- op:" in c["text"] for c in chunks)
    hold = [c for c in chunks if c["ku_id"] == "KU-PAY-hold-funds" and c["source_path"] == "docs/core-platform/hold-funds.md"]
    assert hold


def test_operation_kept_with_its_tables(chunks):
    op = [c for c in chunks if c["operation"] == "PostPciCardsV1"]
    assert op and all(c["ku_id"] == "KU-API-migrations--card-migration" for c in op)
    body = [c for c in op if "request-body" in c["chunk_id"]][0]["text"]
    assert "encrypted_pan" in body and "| Field | Type | Required | Description | Constraints |" in body


def test_split_tables_repeat_header():
    rows = "\n".join(f"| r{i} | {'x' * 50} |" for i in range(200))
    body = f"# T\n\n## Big table\n\n| A | B |\n| --- | --- |\n{rows}\n"
    parts = corpus.chunk_ku(make_ku(body=body))
    tparts = [p for p in parts if "| r" in p["text"]]
    assert len(tparts) > 1
    assert all("| A | B |" in p["text"] for p in tparts)
    assert all(p["chars"] <= corpus.MAX_CHARS for p in parts)


def test_split_code_fences_reopen():
    code = "\n".join(f"line {i} " + "y" * 60 for i in range(200))
    body = f"# T\n\n## Code\n\n```json\n{code}\n```\n"
    parts = [p for p in corpus.chunk_ku(make_ku(body=body)) if "line" in p["text"]]
    assert len(parts) > 1
    assert all(p["text"].count("```") % 2 == 0 for p in parts)


def test_manifest_hash_reproducible(summary):
    with open(os.path.join(EXP, "CORPUS_MANIFEST.csv"), encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) == 623
    for r in rows[:: 25]:
        with open(os.path.join(MIG, r["ku_path"]), "rb") as fh:
            assert sha_bytes(fh.read()) == r["sha256"]
    h = sha_bytes("".join(f"{r['ku_path']}\t{r['sha256']}\n" for r in sorted(rows, key=lambda r: r["ku_path"])).encode())
    assert h == summary["corpus_manifest_hash"]


def test_chunk_set_hash_reproducible(chunks, summary):
    assert sha_bytes("".join(f"{c['chunk_id']}\t{c['sha256']}\n" for c in chunks).encode()) == summary["chunk_set_hash"]
