import uuid
from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Index, Integer, String, Text, UniqueConstraint, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.base import Base, JSONType, utcnow

ROLES = ("user", "assistant")
# pipeline statuses + "no_evidence" + "error" (generation failed / timed out; content is empty, never fabricated)
ASSISTANT_STATUSES = ("answered", "partial", "not_documented", "conflicting_sources", "no_evidence", "error")


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    session_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("sessions.id", ondelete="CASCADE"), nullable=False)
    seq: Mapped[int] = mapped_column(Integer, nullable=False)  # position within the session (chronological order)
    role: Mapped[str] = mapped_column(String(16), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str | None] = mapped_column(String(32), nullable=True)      # assistant messages only
    citations: Mapped[list | None] = mapped_column(JSONType, nullable=True)    # validated citations from the pipeline
    details: Mapped[dict | None] = mapped_column(JSONType, nullable=True)      # warnings, verification, evidence ids, context, error
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=utcnow, server_default=func.now())

    session = relationship("ChatSession", back_populates="messages")

    __table_args__ = (
        UniqueConstraint("session_id", "seq", name="uq_messages_session_seq"),
        CheckConstraint("role IN ('user', 'assistant')", name="ck_messages_role"),
        CheckConstraint("(role = 'user' AND status IS NULL) OR (role = 'assistant' AND status IN "
                        "('answered', 'partial', 'not_documented', 'conflicting_sources', 'no_evidence', 'error'))",
                        name="ck_messages_status"),
        CheckConstraint("seq >= 1", name="ck_messages_seq_positive"),
        Index("ix_messages_session_seq", "session_id", "seq"),
    )
