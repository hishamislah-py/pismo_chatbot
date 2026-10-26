"""Safety of the test configuration itself. No real database is touched: destructive operations are mocks."""
import os

import pytest

from backend.tests.pg_safety import UnsafeTestDatabase, prepare_test_database, validate_test_database_url

GOOD = "postgresql+psycopg://pismo_app:not-a-real-password@localhost:5434/pismo_assistant_test"


@pytest.mark.parametrize("raw, reason", [
    (None, "not set"),
    ("", "not set"),
    ("   ", "not set"),
    ("postgresql+psycopg://pismo_app:x@localhost:5434/pismo_assistant", "development database"),
    ("postgresql+psycopg://pismo_app:x@localhost:5434/pismo_assistant_dev", "does not end with '_test'"),
    ("postgresql+psycopg://pismo_app:x@localhost:5434/postgres", "does not end with '_test'"),
    ("postgresql+psycopg://pismo_app:x@localhost:5434/", "does not name a database"),
    ("postgresql+psycopg://pismo_app:x@localhost:5434", "does not name a database"),
    ("not a url at all", "could not be parsed"),
    ("://missing-driver/x_test", "could not be parsed"),
    ("sqlite:///pismo_assistant_test", "must be a PostgreSQL URL"),
    ("mysql+pymysql://u:p@localhost/pismo_assistant_test", "must be a PostgreSQL URL"),
])
def test_unsafe_urls_rejected(raw, reason):
    with pytest.raises(UnsafeTestDatabase, match=reason) as e:
        validate_test_database_url(raw)
    assert "not-a-real-password" not in str(e.value) and ":x@" not in str(e.value)   # no credentials in messages


def test_valid_test_database_passes():
    url = validate_test_database_url(GOOD)
    assert url.database == "pismo_assistant_test" and url.port == 5434 and url.get_backend_name() == "postgresql"


def test_app_configured_database_is_also_rejected():
    with pytest.raises(UnsafeTestDatabase, match="development database"):
        validate_test_database_url("postgresql+psycopg://u:p@localhost:5434/shared_test", app_database_name="shared_test")


class Recorder:
    def __init__(self):
        self.calls = []

    def __call__(self, name):
        def f(*a, **k):
            self.calls.append(name)
            return object()
        return f


@pytest.mark.parametrize("raw", [None, "postgresql+psycopg://u:p@localhost:5434/pismo_assistant",
                                 "postgresql+psycopg://u:p@localhost:5434/other", "garbage"])
def test_rejected_configs_never_reach_destructive_operations(raw):
    rec = Recorder()
    with pytest.raises(UnsafeTestDatabase):
        prepare_test_database(raw, downgrade=rec("downgrade"), upgrade=rec("upgrade"),
                              create_engine=rec("create_engine"), alembic_config=rec("alembic_config"))
    assert rec.calls == []


def test_valid_config_runs_reset_in_order_with_mocks():
    rec = Recorder()
    prepare_test_database(GOOD, downgrade=rec("downgrade"), upgrade=rec("upgrade"),
                          create_engine=rec("create_engine"), alembic_config=rec("alembic_config"))
    assert rec.calls == ["alembic_config", "downgrade", "upgrade", "create_engine"]


# ---------- regular tests cannot reach PostgreSQL
def test_regular_tests_settings_point_at_sqlite():
    from backend.app.core.config import get_settings
    assert os.environ["DATABASE_URL"] == "sqlite://"
    assert get_settings().database_url == "sqlite://"     # not the URL derived from PISMO_DB_APP_PASSWORD in .env


def test_lazy_fallback_cannot_create_postgres_engine():
    from backend.app.db import session as db_session
    with pytest.raises(RuntimeError, match="SQLite only"):
        db_session.make_engine("postgresql+psycopg://u:p@localhost:5434/pismo_assistant")


def test_lazy_fallback_without_engine_resolves_to_sqlite():
    from backend.app.db import session as db_session
    db_session.configure(engine=None)
    try:
        eng = db_session.get_engine()                      # the fallback used when no fixture engine is configured
        assert eng is not None and eng.dialect.name == "sqlite" and eng.url.database in (None, "", ":memory:")
    finally:
        db_session.configure(engine=None)


def test_integration_target_is_not_read_from_dotenv():
    import backend.tests.conftest as c
    from backend.tests import test_postgres  # noqa: F401  (module imports fine even when skipped)
    assert c.PROCESS_TEST_DATABASE_URL == os.environ.get("TEST_DATABASE_URL")
