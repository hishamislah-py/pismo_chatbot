"""Test fixtures: SQLite (in-memory, shared connection) + a mocked pipeline. No OpenAI calls, no PostgreSQL needed.
PostgreSQL-specific tests live in test_postgres.py and run only when TEST_DATABASE_URL is set in the process
environment and passes the checks in pg_safety.py."""
import os
import sys
from pathlib import Path

# Captured before anything can load .env: the integration-test target may only come from the real process environment.
PROCESS_TEST_DATABASE_URL = os.environ.get("TEST_DATABASE_URL")
# Regular tests must never fall back to the development PostgreSQL database: an explicit DATABASE_URL in the environment
# takes precedence over .env (and over the URL derived from PISMO_DB_APP_PASSWORD), so pin it to in-memory SQLite.
os.environ["DATABASE_URL"] = "sqlite://"
os.environ["ASSISTANT_PRELOAD"] = "false"          # never load the real index/model in tests
os.environ["ROUTER_ENABLED"] = "false"             # never build a real routing classifier; tests inject fakes
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from sqlalchemy import create_engine, event  # noqa: E402
from sqlalchemy.pool import StaticPool  # noqa: E402

from backend.app import models  # noqa: E402,F401
from backend.app.core.config import Settings, get_settings  # noqa: E402
from backend.app.db import session as db_session  # noqa: E402
from backend.app.db.base import Base  # noqa: E402
from backend.app.main import create_app  # noqa: E402
from backend.app.services.assistant_service import AssistantService, get_assistant_service  # noqa: E402

get_settings.cache_clear()                          # settings must reflect the pinned DATABASE_URL


def pytest_configure(config):
    config.addinivalue_line("markers", "postgres: integration test that may use the explicitly configured test PostgreSQL database")


@pytest.fixture(autouse=True)
def forbid_non_sqlite_engines(request, monkeypatch):
    """Outside @pytest.mark.postgres tests, the app may only create SQLite engines (guards the lazy DATABASE_URL fallback
    in backend.app.db.session.get_engine)."""
    if request.node.get_closest_marker("postgres"):
        yield
        return
    real = db_session.make_engine

    def guarded(url):
        from sqlalchemy.engine import make_url
        if make_url(url).get_backend_name() != "sqlite":
            raise RuntimeError(f"regular tests may not create a '{make_url(url).get_backend_name()}' engine (SQLite only)")
        return real(url)
    monkeypatch.setattr(db_session, "make_engine", guarded)
    yield


def pipeline_result(answer="Use `POST /payment-methods/v2/transfers` [E1].", status="answered", citations=None, **extra):
    """Shape of pismo_assistant.pipeline.Assistant.answer() output (fields the backend reads)."""
    cites = citations if citations is not None else [{
        "label": "E1", "ku_id": "KU-API-core-platform-payment-methods--payment-methods-part-02",
        "title": "API reference: Core platform - Payment methods (part 2)", "section": "Operation contracts > `POST /payment-methods/v2/transfers` — Create transfer",
        "chunk_id": "KU-API-core-platform-payment-methods--payment-methods-part-02::op-post-transfers", "origin": "named_operation",
        "sources": [{"path": "api-specs/Core_platform_-_Payment_methods.yaml", "url": "https://github.com/PismoDevEx/pismo-api-specs"}]}]
    r = {"status": status, "answer": answer, "citations": cites, "warnings": [], "citations_valid": True,
         "verification": {"source_mapping": True, "semantic_support_verified": False}, "model": "fake-model",
         "missing_information": "", "matched_operations": [], "error": None,
         "evidence": [{"label": "E1", "chunk_id": cites[0]["chunk_id"] if cites else "x", "ku_id": "KU-X", "origin": "retrieved",
                       "text_not_returned": True}]}
    r.update(extra)
    return r


class FakePipeline:
    def __init__(self, results=None, exc=None, delay=0.0):
        self.results = list(results or [pipeline_result()])
        self.exc, self.delay, self.questions = exc, delay, []

    def answer(self, question):
        import time
        self.questions.append(question)
        if self.delay:
            time.sleep(self.delay)
        if self.exc:
            raise self.exc
        return self.results.pop(0) if len(self.results) > 1 else self.results[0]


@pytest.fixture
def engine():
    eng = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)

    @event.listens_for(eng, "connect")
    def _fk(dbapi_conn, _):
        dbapi_conn.execute("PRAGMA foreign_keys=ON")
    Base.metadata.create_all(eng)
    db_session.configure(engine=eng)
    yield eng
    db_session.configure(engine=None)
    eng.dispose()


@pytest.fixture
def settings():
    return Settings(DATABASE_URL="sqlite://", ASSISTANT_PRELOAD=False, CONTEXT_MAX_PRIOR_QUESTIONS=2, CONTEXT_MAX_CHARS=600)


@pytest.fixture
def make_client(engine, settings):
    clients = []

    def _make(pipeline=None, timeout_s=5.0, settings_override=None):
        app = create_app()
        fake = pipeline or FakePipeline()
        svc = AssistantService(pipeline=fake, timeout_s=timeout_s)
        app.dependency_overrides[get_assistant_service] = lambda: svc
        app.dependency_overrides[get_settings] = lambda: settings_override or settings
        c = TestClient(app)
        c.pipeline = fake
        clients.append(c)
        return c
    yield _make
    for c in clients:
        c.close()


@pytest.fixture
def client(make_client):
    return make_client()
