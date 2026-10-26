"""PostgreSQL integration tests. DESTRUCTIVE for the target: every table in it is dropped and recreated.

They run only when TEST_DATABASE_URL is set in the PROCESS environment (never read from .env) and passes pg_safety
(PostgreSQL, database name ends with "_test", not the development database "pismo_assistant"). Example for the
Docker database (set in the current PowerShell session only; do not store real passwords in files or docs):
    $env:TEST_DATABASE_URL = 'postgresql+psycopg://pismo_app:<password>@127.0.0.1:5434/pismo_assistant_test'
(Use 127.0.0.1, not localhost: on this machine localhost tries IPv6 ::1 first and stalls ~10 s per connection.)
If TEST_DATABASE_URL is not set, the module is skipped and reported as such. If it is set but unsafe, every test in this
module fails with the reason before any connection is made."""
import uuid

import pytest

from backend.tests.conftest import PROCESS_TEST_DATABASE_URL
from backend.tests.pg_safety import UnsafeTestDatabase, prepare_test_database

pytestmark = [pytest.mark.postgres,
              pytest.mark.skipif(not PROCESS_TEST_DATABASE_URL,
                                 reason="TEST_DATABASE_URL not set in the process environment - PostgreSQL integration tests skipped")]


@pytest.fixture(scope="module")
def pg_engine():
    from alembic import command
    from sqlalchemy import create_engine
    from backend.tests.test_db import alembic_cfg
    try:   # validation happens inside prepare_test_database BEFORE any connection, downgrade or upgrade
        _, cfg, eng = prepare_test_database(PROCESS_TEST_DATABASE_URL, downgrade=command.downgrade, upgrade=command.upgrade,
                                            create_engine=create_engine, alembic_config=alembic_cfg)
    except UnsafeTestDatabase as e:
        pytest.fail(f"Refusing to run destructive PostgreSQL tests: {e}", pytrace=False)
    yield eng
    eng.dispose()
    command.downgrade(cfg, "base")


def test_pg_schema_and_types(pg_engine):
    from sqlalchemy import inspect, text
    insp = inspect(pg_engine)
    assert {"sessions", "messages", "activity"} <= set(insp.get_table_names())
    cols = {c["name"]: str(c["type"]) for c in insp.get_columns("messages")}
    assert cols["id"] == "UUID" and cols["citations"] == "JSONB" and cols["details"] == "JSONB"
    fks = insp.get_foreign_keys("messages")
    assert fks[0]["referred_table"] == "sessions" and fks[0]["options"].get("ondelete") == "CASCADE"
    with pg_engine.connect() as conn:
        assert conn.execute(text("select version_num from alembic_version")).scalar() == "0001_initial"


def test_pg_constraints_and_cascade(pg_engine):
    from sqlalchemy import select
    from sqlalchemy.exc import IntegrityError
    from sqlalchemy.orm import Session
    from backend.app.models import Activity, ChatSession, Message
    with Session(pg_engine) as db:
        s = ChatSession(title="pg")
        db.add(s)
        db.commit()
        db.add(Message(session_id=s.id, role="system", content="x", seq=1))
        with pytest.raises(IntegrityError):
            db.commit()
        db.rollback()
        db.add_all([Message(session_id=s.id, role="user", content="q", seq=1),
                    Message(session_id=s.id, role="assistant", content="a", seq=2, status="answered",
                            citations=[{"label": "E1", "ku_id": "KU-X"}], details={"k": 1})])
        db.add(Activity(session_id=s.id, event="message.answer", status="answered", http_status=201, duration_ms=5))
        db.commit()
        sid = s.id
        db.delete(db.get(ChatSession, sid))
        db.commit()
        assert db.scalars(select(Message).where(Message.session_id == sid)).all() == []
        assert all(a.session_id is None for a in db.scalars(select(Activity)))


def test_pg_api_flow(pg_engine, make_client):
    from backend.app.db import session as db_session
    c = make_client()
    db_session.configure(engine=pg_engine)     # make_client's engine fixture configured SQLite; point the app at PostgreSQL
    s = c.post("/api/sessions").json()["id"]
    r = c.post(f"/api/sessions/{s}/messages", json={"content": "How do I create a transfer?"})
    assert r.status_code == 201
    c.post(f"/api/sessions/{s}/messages", json={"content": "What about the required fields?"})
    msgs = c.get(f"/api/sessions/{s}/messages").json()["messages"]
    assert [m["seq"] for m in msgs] == [1, 2, 3, 4] and msgs[1]["citations"][0]["label"] == "E1"
    assert '"How do I create a transfer?"' in c.pipeline.questions[-1]
    assert c.get("/api/health").json()["database"] == "ok"
    assert c.delete(f"/api/sessions/{s}").status_code == 204
    assert uuid.UUID(s)
