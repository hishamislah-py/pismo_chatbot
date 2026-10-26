"""Engine and session factory. The engine is created lazily from DATABASE_URL; tables are created by Alembic
migrations only (never at application start-up)."""
from collections.abc import Iterator

from fastapi import HTTPException
from sqlalchemy import create_engine, event, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from ..core.config import get_settings

_engine: Engine | None = None
_factory: sessionmaker | None = None


def make_engine(url: str) -> Engine:
    kwargs = {"pool_pre_ping": True}
    if url.startswith("sqlite"):
        kwargs = {"connect_args": {"check_same_thread": False}}
    engine = create_engine(url, **kwargs)
    if url.startswith("sqlite"):
        @event.listens_for(engine, "connect")
        def _fk_on(dbapi_conn, _):  # SQLite enforces ON DELETE CASCADE only with this pragma
            dbapi_conn.execute("PRAGMA foreign_keys=ON")
    return engine


def configure(url: str | None = None, engine: Engine | None = None) -> None:
    """(Re)configure the engine. Used at start-up and by tests."""
    global _engine, _factory
    _engine = engine or (make_engine(url) if url else None)
    _factory = sessionmaker(bind=_engine, expire_on_commit=False) if _engine else None


def get_engine() -> Engine | None:
    if _engine is None and get_settings().database_url:
        configure(get_settings().database_url)
    return _engine


def get_db() -> Iterator[Session]:
    if get_engine() is None or _factory is None:
        raise HTTPException(status_code=503, detail={"code": "database_not_configured",
                                                     "message": "DATABASE_URL is not set; see .env.example"})
    db = _factory()
    try:
        yield db
    finally:
        db.close()


def database_status() -> str:
    """'ok', 'unavailable' or 'not_configured' - never the URL or the error text (which may contain credentials)."""
    engine = get_engine()
    if engine is None:
        return "not_configured"
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return "ok"
    except Exception:
        return "unavailable"
