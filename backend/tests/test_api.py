"""API workflow tests (SQLite + mocked pipeline)."""
import uuid

from sqlalchemy import select

from backend.app.models import Activity, Message
from backend.tests.conftest import FakePipeline, pipeline_result


def new_session(client, **body):
    r = client.post("/api/sessions", json=body or None)
    assert r.status_code == 201, r.text
    return r.json()


# ---------------- health
def test_health_reports_components_without_secrets(client):
    r = client.get("/api/health")
    assert r.status_code == 200
    body = r.json()
    # the injected fake pipeline has no retriever, so no index version is known (null, never invented)
    assert body == {"status": "ok", "app": "ok", "database": "ok", "assistant": "loaded", "index": {"chunk_set_hash": None}}
    assert "sqlite" not in r.text and "postgres" not in r.text.lower() and "key" not in r.text.lower()


def test_health_without_database(make_client, engine):
    from backend.app.db import session as db_session
    c = make_client()
    db_session.configure(engine=None)
    import backend.app.db.session as s
    orig = s.get_settings
    s.get_settings = lambda: type("S", (), {"database_url": None})()
    try:
        body = c.get("/api/health").json()
        assert body["database"] == "not_configured" and body["status"] == "degraded"
        r = c.get("/api/sessions")
        assert r.status_code == 503 and r.json()["detail"]["code"] == "database_not_configured"
    finally:
        s.get_settings = orig


# ---------------- sessions
def test_create_list_get_session(client):
    a = new_session(client)
    b = new_session(client, title="Transfers")
    assert a["title"] is None and b["title"] == "Transfers" and a["message_count"] == 0
    client.post(f"/api/sessions/{a['id']}/messages", json={"content": "How do I create a transfer?"})
    listed = client.get("/api/sessions").json()["sessions"]
    assert [s["id"] for s in listed] == [a["id"], b["id"]]          # newest activity first
    assert listed[0]["message_count"] == 2
    got = client.get(f"/api/sessions/{a['id']}").json()
    assert got["title"] == "How do I create a transfer?"             # derived from the first question
    assert got["message_count"] == 2


def test_unknown_session_ids(client):
    sid = uuid.uuid4()
    assert client.get(f"/api/sessions/{sid}").status_code == 404
    assert client.get(f"/api/sessions/{sid}/messages").status_code == 404
    r = client.post(f"/api/sessions/{sid}/messages", json={"content": "hi there"})
    assert r.status_code == 404 and r.json()["detail"]["code"] == "session_not_found"
    assert client.pipeline.questions == []                          # pipeline never called for unknown sessions
    assert client.delete(f"/api/sessions/{sid}").status_code == 404
    assert client.get("/api/sessions/not-a-uuid").status_code == 422


def test_delete_session_removes_messages(client, engine):
    s = new_session(client)
    client.post(f"/api/sessions/{s['id']}/messages", json={"content": "How do I create a transfer?"})
    other = new_session(client)
    client.post(f"/api/sessions/{other['id']}/messages", json={"content": "What does WEAM0029 mean?"})
    assert client.delete(f"/api/sessions/{s['id']}").status_code == 204
    assert client.get(f"/api/sessions/{s['id']}").status_code == 404
    from sqlalchemy.orm import Session
    with Session(engine) as db:
        sids = {m.session_id for m in db.scalars(select(Message))}
        assert sids == {uuid.UUID(other["id"])}                      # other session untouched
        assert all(a.session_id != uuid.UUID(s["id"]) for a in db.scalars(select(Activity)))  # SET NULL on delete


# ---------------- messages
def test_message_exchange_persists_in_order_with_citations(client):
    s = new_session(client)
    r = client.post(f"/api/sessions/{s['id']}/messages", json={"content": "  How do I create a transfer?  "})
    assert r.status_code == 201, r.text
    ex = r.json()
    assert ex["user_message"]["content"] == "How do I create a transfer?" and ex["user_message"]["seq"] == 1
    a = ex["assistant_message"]
    assert a["role"] == "assistant" and a["seq"] == 2 and a["status"] == "answered"
    assert a["citations"][0]["ku_id"] == "KU-API-core-platform-payment-methods--payment-methods-part-02"
    assert a["citations"][0]["sources"][0]["url"].startswith("https://")
    assert a["details"]["citations_valid"] is True and a["details"]["verification"]["semantic_support_verified"] is False
    client.post(f"/api/sessions/{s['id']}/messages", json={"content": "What does WEAM0029 mean?"})
    hist = client.get(f"/api/sessions/{s['id']}/messages").json()["messages"]
    assert [(m["seq"], m["role"]) for m in hist] == [(1, "user"), (2, "assistant"), (3, "user"), (4, "assistant")]
    assert hist[1]["citations"] == a["citations"]                    # citations round-trip unchanged


def test_citation_metadata_is_not_invented(make_client):
    c = make_client(FakePipeline([pipeline_result(answer="Not documented [E1].", status="not_documented", citations=[])]))
    s = new_session(c)
    a = c.post(f"/api/sessions/{s['id']}/messages", json={"content": "How do I perform PCI card go-live?"}).json()["assistant_message"]
    assert a["status"] == "not_documented" and a["citations"] == []


def test_no_evidence_status_is_persisted(make_client):
    c = make_client(FakePipeline([pipeline_result(answer="No knowledge-unit passages were retrieved.", status="no_evidence", citations=[])]))
    s = new_session(c)
    r = c.post(f"/api/sessions/{s['id']}/messages", json={"content": "zzzz qqqq"})
    assert r.status_code == 201 and r.json()["assistant_message"]["status"] == "no_evidence"


def test_invalid_input(client):
    s = new_session(client)
    url = f"/api/sessions/{s['id']}/messages"
    assert client.post(url, json={"content": "   "}).status_code == 422
    assert client.post(url, json={}).status_code == 422
    assert client.post(url, json={"content": "ok question", "role": "assistant"}).status_code == 422   # extra fields rejected
    assert client.post(url, json={"content": "x" * 2001}).status_code == 422
    assert client.post("/api/sessions", json={"title": "t" * 201}).status_code == 422
    assert client.get(url).json()["messages"] == []                  # nothing persisted for invalid requests


def test_oversized_request_rejected(client):
    s = new_session(client)
    r = client.post(f"/api/sessions/{s['id']}/messages", content=b'{"content": "' + b"a" * 20000 + b'"}',
                    headers={"content-type": "application/json"})
    assert r.status_code == 413 and r.json()["detail"]["code"] == "request_too_large"


# ---------------- failures
def test_generation_error_records_failure_without_fabricated_answer(make_client, engine):
    err = {"status": "generation_error", "answer": "", "citations": [], "warnings": [], "evidence": [{"label": "E1"}],
           "error": {"kind": "api_error", "message": "APIConnectionError: Connection error."}}
    c = make_client(FakePipeline([err]))
    s = new_session(c)
    r = c.post(f"/api/sessions/{s['id']}/messages", json={"content": "How do I create a transfer?"})
    assert r.status_code == 502
    a = r.json()["assistant_message"]
    assert a["status"] == "error" and a["content"] == "" and a["citations"] == []
    assert a["details"]["error"]["kind"] == "api_error"
    hist = c.get(f"/api/sessions/{s['id']}/messages").json()["messages"]
    assert [(m["role"], m["status"]) for m in hist] == [("user", None), ("assistant", "error")]   # exactly one of each


def test_missing_openai_key_maps_to_503(make_client):
    err = {"status": "generation_error", "answer": "", "citations": [], "evidence": [],
           "error": {"kind": "configuration", "message": "OPENAI_API_KEY is not set"}}
    c = make_client(FakePipeline([err]))
    s = new_session(c)
    assert c.post(f"/api/sessions/{s['id']}/messages", json={"content": "How do I create a transfer?"}).status_code == 503


def test_timeout(make_client):
    c = make_client(FakePipeline(delay=1.0), timeout_s=0.2)
    s = new_session(c)
    r = c.post(f"/api/sessions/{s['id']}/messages", json={"content": "How do I create a transfer?"})
    assert r.status_code == 504
    a = r.json()["assistant_message"]
    assert a["status"] == "error" and a["content"] == "" and a["details"]["error"]["kind"] == "timeout"
    assert len(c.get(f"/api/sessions/{s['id']}/messages").json()["messages"]) == 2


def test_unexpected_pipeline_exception(make_client):
    c = make_client(FakePipeline(exc=RuntimeError("boom with secret-looking text sk-123")))
    s = new_session(c)
    r = c.post(f"/api/sessions/{s['id']}/messages", json={"content": "How do I create a transfer?"})
    assert r.status_code == 500
    a = r.json()["assistant_message"]
    assert a["status"] == "error" and a["details"]["error"] == {"kind": "internal", "message": "RuntimeError"}
    assert "sk-123" not in r.text                                    # exception text is not echoed


# ---------------- activity
def test_activity_log(make_client):
    c = make_client(FakePipeline([pipeline_result(), {"status": "generation_error", "answer": "", "citations": [], "evidence": [],
                                                      "error": {"kind": "malformed_output", "message": "not JSON"}}]))
    s = new_session(c)
    c.post(f"/api/sessions/{s['id']}/messages", json={"content": "How do I create a transfer?"})
    c.post(f"/api/sessions/{s['id']}/messages", json={"content": "What does WEAM0029 mean?"})
    act = c.get("/api/activity").json()["activity"]
    assert len(act) == 2
    by = {a["status"]: a for a in act}
    assert by["answered"]["http_status"] == 201 and by["answered"]["citation_count"] == 1 and by["answered"]["evidence_count"] == 1
    assert by["malformed_output"]["http_status"] == 502 and by["malformed_output"]["error_kind"] == "malformed_output"
    assert all(a["session_id"] == s["id"] and a["duration_ms"] >= 0 for a in act)
    assert "transfer" not in str(act).lower()                        # no question text in the activity log
