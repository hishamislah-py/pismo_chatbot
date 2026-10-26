"""Constraints and migrations on SQLite (always run). PostgreSQL equivalents are in test_postgres.py."""
import uuid

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.models import ChatSession, Message
from backend.tests.conftest import ROOT


def alembic_cfg(url):
    cfg = Config(str(ROOT / "backend" / "alembic.ini"))
    cfg.set_main_option("sqlalchemy.url", url)
    return cfg


def test_migration_upgrade_and_downgrade_sqlite(tmp_path):
    url = f"sqlite:///{tmp_path / 'm.db'}"
    command.upgrade(alembic_cfg(url), "head")
    insp = inspect(create_engine(url))
    assert {"sessions", "messages", "activity", "alembic_version"} <= set(insp.get_table_names())
    assert {c["name"] for c in insp.get_check_constraints("messages")} >= {"ck_messages_role", "ck_messages_status"}
    assert {i["name"] for i in insp.get_indexes("messages")} >= {"ix_messages_session_seq"}
    command.downgrade(alembic_cfg(url), "base")
    assert set(inspect(create_engine(url)).get_table_names()) == {"alembic_version"}


def test_constraints(engine):
    with Session(engine) as db:
        s = ChatSession()
        db.add(s)
        db.commit()
        for bad in (dict(role="system", content="x", seq=1), dict(role="user", content="x", seq=1, status="answered"),
                    dict(role="assistant", content="x", seq=1, status="made_up"), dict(role="user", content="x", seq=0)):
            db.add(Message(session_id=s.id, **bad))
            with pytest.raises(IntegrityError):
                db.commit()
            db.rollback()
        db.add(Message(session_id=s.id, role="user", content="x", seq=1))
        db.commit()
        db.add(Message(session_id=s.id, role="user", content="y", seq=1))     # duplicate position in the session
        with pytest.raises(IntegrityError):
            db.commit()
        db.rollback()
        db.add(Message(session_id=uuid.uuid4(), role="user", content="orphan", seq=1))  # FK
        with pytest.raises(IntegrityError):
            db.commit()
