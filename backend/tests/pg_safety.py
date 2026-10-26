"""Safety gate for the destructive PostgreSQL integration tests (they drop and recreate every table in the target).

The target comes ONLY from TEST_DATABASE_URL in the real process environment, captured by conftest.py before any
module could load .env. It is parsed with SQLAlchemy's URL parser and must:
  * be a PostgreSQL URL,
  * name a database,
  * use a database name ending in "_test",
  * not be the development database "pismo_assistant" (nor the database the app is configured to use).
Errors never include the URL, user or password - only the database name and driver.
"""
from sqlalchemy.engine import URL, make_url
from sqlalchemy.exc import ArgumentError

DEV_DATABASE = "pismo_assistant"
REQUIRED_SUFFIX = "_test"
HOW_TO = ("Set it in this PowerShell session only, for example: "
          "$env:TEST_DATABASE_URL = 'postgresql+psycopg://pismo_app:<password>@127.0.0.1:5434/pismo_assistant_test'")


class UnsafeTestDatabase(Exception):
    pass


def validate_test_database_url(raw: str | None, app_database_name: str | None = None) -> URL:
    if raw is None or not raw.strip():
        raise UnsafeTestDatabase(f"TEST_DATABASE_URL is not set in the process environment. {HOW_TO}")
    try:
        url = make_url(raw.strip())
    except (ArgumentError, ValueError) as e:
        raise UnsafeTestDatabase(f"TEST_DATABASE_URL could not be parsed as a database URL ({type(e).__name__}). {HOW_TO}") from None
    if url.get_backend_name() != "postgresql":
        raise UnsafeTestDatabase(f"TEST_DATABASE_URL must be a PostgreSQL URL (got driver '{url.drivername}').")
    db = (url.database or "").strip()
    if not db:
        raise UnsafeTestDatabase("TEST_DATABASE_URL does not name a database. Use a disposable database such as pismo_assistant_test.")
    if db == DEV_DATABASE or (app_database_name and db == app_database_name):
        raise UnsafeTestDatabase(f"TEST_DATABASE_URL targets the development database '{db}'. The integration tests drop all "
                                 f"tables; point them at a separate database such as {DEV_DATABASE}{REQUIRED_SUFFIX}.")
    if not db.endswith(REQUIRED_SUFFIX):
        raise UnsafeTestDatabase(f"TEST_DATABASE_URL database '{db}' does not end with '{REQUIRED_SUFFIX}'. Only databases "
                                 f"explicitly named as test databases may be dropped and recreated.")
    return url


def app_database_name() -> str | None:
    """Name of the database the application is configured to use (from settings), or None. Used only for comparison."""
    try:
        from backend.app.core.config import Settings
        u = Settings().database_url
        return make_url(u).database if u else None
    except Exception:
        return None


def prepare_test_database(raw: str | None, *, downgrade, upgrade, create_engine, alembic_config):
    """Validate FIRST, then reset the schema with Alembic and return an engine. The callables are injected so the
    order (validation before any connection or drop) can be tested without a database."""
    url = validate_test_database_url(raw, app_database_name())
    cfg = alembic_config(url.render_as_string(hide_password=False))
    downgrade(cfg, "base")
    upgrade(cfg, "head")
    return url, cfg, create_engine(url)
