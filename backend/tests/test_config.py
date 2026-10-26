"""Database URL derivation for the Docker Compose database (no real secrets used)."""
from backend.app.core.config import Settings


def test_url_derived_from_compose_password_and_url_encoded():
    # DATABASE_URL="" overrides the sqlite:// pin that conftest.py sets in the test process environment
    s = Settings(_env_file=None, DATABASE_URL="", PISMO_DB_APP_PASSWORD="p@ss:w/rd#1", PISMO_DB_HOST_PORT=5434)
    assert s.database_url == "postgresql+psycopg://pismo_app:p%40ss%3Aw%2Frd%231@127.0.0.1:5434/pismo_assistant"
    assert "p@ss" not in repr(s)                      # password field is excluded from repr


def test_derived_url_host_defaults_to_ipv4_loopback_and_is_overridable():
    s = Settings(_env_file=None, DATABASE_URL="", PISMO_DB_APP_PASSWORD="x")
    assert "@127.0.0.1:5434/" in s.database_url and "localhost" not in s.database_url
    s = Settings(_env_file=None, DATABASE_URL="", PISMO_DB_APP_PASSWORD="x", PISMO_DB_HOST="db.internal", PISMO_DB_HOST_PORT=6000)
    assert s.database_url.endswith("@db.internal:6000/pismo_assistant")


def test_explicit_database_url_wins():
    s = Settings(_env_file=None, DATABASE_URL="postgresql+psycopg://u:x@db:5432/other", PISMO_DB_APP_PASSWORD="y")
    assert s.database_url == "postgresql+psycopg://u:x@db:5432/other"


def test_no_database_configured():
    assert Settings(_env_file=None, DATABASE_URL="").database_url is None
