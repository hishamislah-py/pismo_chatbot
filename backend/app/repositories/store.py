"""Focused persistence functions for sessions, messages and activity. Callers own the transaction (commit)."""
import uuid
from collections.abc import Callable

from sqlalchemy import delete, func, select
from sqlalchemy.orm import Session

from ..db.base import utcnow
from ..models import Activity, ChatSession, Message


# ---- sessions
def create_session(db: Session, title: str | None = None) -> ChatSession:
    s = ChatSession(title=title)
    db.add(s)
    db.flush()
    return s


def get_session(db: Session, session_id: uuid.UUID) -> ChatSession | None:
    return db.get(ChatSession, session_id)


def session_exists(db: Session, session_id: uuid.UUID) -> bool:
    """Queries the database (db.get() could answer from the identity map with an object loaded earlier)."""
    return db.scalar(select(ChatSession.id).where(ChatSession.id == session_id)) is not None


def list_sessions(db: Session, limit: int = 100) -> list[tuple[ChatSession, int]]:
    counts = select(Message.session_id, func.count(Message.id).label("n")).group_by(Message.session_id).subquery()
    rows = db.execute(select(ChatSession, func.coalesce(counts.c.n, 0))
                      .outerjoin(counts, counts.c.session_id == ChatSession.id)
                      .order_by(ChatSession.updated_at.desc(), ChatSession.created_at.desc()).limit(limit)).all()
    return [(s, n) for s, n in rows]


def count_messages(db: Session, session_id: uuid.UUID) -> int:
    return db.scalar(select(func.count(Message.id)).where(Message.session_id == session_id)) or 0


def delete_session(db: Session, session_id: uuid.UUID) -> bool:
    # messages are removed by ON DELETE CASCADE; delete them explicitly too so behaviour does not depend on the driver
    db.execute(delete(Message).where(Message.session_id == session_id))
    return db.execute(delete(ChatSession).where(ChatSession.id == session_id)).rowcount > 0


def touch_session(db: Session, s: ChatSession, first_question: str | None = None) -> None:
    s.updated_at = utcnow()
    if not s.title and first_question:
        t = " ".join(first_question.split())
        s.title = t if len(t) <= 80 else t[:77].rstrip() + "..."


# ---- messages
def list_messages(db: Session, session_id: uuid.UUID) -> list[Message]:
    return list(db.scalars(select(Message).where(Message.session_id == session_id).order_by(Message.seq)))


def next_seq(db: Session, session_id: uuid.UUID) -> int:
    return (db.scalar(select(func.max(Message.seq)).where(Message.session_id == session_id)) or 0) + 1


def add_message(db: Session, session_id: uuid.UUID, role: str, content: str, status: str | None = None,
                citations: list | None = None, details: dict | None = None) -> Message:
    m = Message(session_id=session_id, seq=next_seq(db, session_id), role=role, content=content, status=status,
                citations=citations, details=details)
    db.add(m)
    db.flush()
    return m


def prior_user_questions(db: Session, session_id: uuid.UUID, before_seq: int, limit: int,
                         skip: Callable[[str], bool] | None = None) -> list[Message]:
    """The most recent user messages of THIS session before `before_seq`, oldest first. Never other sessions.
    Messages for which `skip(content)` is true (e.g. greetings) are passed over; the scan is bounded."""
    if limit <= 0:
        return []
    scan = limit if skip is None else limit + 20
    rows = db.scalars(select(Message).where(Message.session_id == session_id, Message.role == "user",
                                            Message.seq < before_seq).order_by(Message.seq.desc()).limit(scan))
    kept = [m for m in rows if skip is None or not skip(m.content)][:limit]
    return list(reversed(kept))


# ---- activity
def add_activity(db: Session, **fields) -> Activity:
    a = Activity(**fields)
    db.add(a)
    db.flush()
    return a


def list_activity(db: Session, limit: int = 50) -> list[Activity]:
    return list(db.scalars(select(Activity).order_by(Activity.created_at.desc()).limit(limit)))
