import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, Integer, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

from ..db.base import Base, utcnow


class Activity(Base):
    """Minimal request activity for the demo. Stores no question/answer text, keys or environment values."""
    __tablename__ = "activity"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=utcnow, server_default=func.now())
    session_id: Mapped[uuid.UUID | None] = mapped_column(Uuid, ForeignKey("sessions.id", ondelete="SET NULL"), nullable=True)
    event: Mapped[str] = mapped_column(String(40), nullable=False)            # e.g. "message.answer"
    status: Mapped[str] = mapped_column(String(32), nullable=False)           # assistant status or error kind
    http_status: Mapped[int] = mapped_column(Integer, nullable=False)
    duration_ms: Mapped[int] = mapped_column(Integer, nullable=False)
    evidence_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    citation_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    model: Mapped[str | None] = mapped_column(String(80), nullable=True)
    error_kind: Mapped[str | None] = mapped_column(String(40), nullable=True)

    __table_args__ = (Index("ix_activity_created_at", "created_at"),)
