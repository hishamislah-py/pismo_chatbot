import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))

from common import EXP, RESULTS, load_json, read_jsonl  # noqa: E402


@pytest.fixture(scope="session")
def chunks():
    return read_jsonl(os.path.join(RESULTS, "chunks.jsonl"))


@pytest.fixture(scope="session")
def bench():
    return load_json(os.path.join(EXP, "BENCHMARK.json"))


@pytest.fixture(scope="session")
def summary():
    return load_json(os.path.join(RESULTS, "corpus_summary.json"))


def make_ku(ku_id="KU-T-x", title="T", body="", sources=None, ku_type="workflow_guide"):
    return {"ku_id": ku_id, "title": title, "category": "c", "ku_type": ku_type, "lifecycle": "current", "path": f"knowledge_units/c/{ku_id}.md",
            "sha256": "0", "bytes": 0, "operations": [], "body": body,
            "sources": sources or [{"path": "docs/a.md", "url": "u", "sha256": "s", "role": "primary_guide"}]}
