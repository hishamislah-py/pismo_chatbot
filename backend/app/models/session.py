import uuid
from datetime import datetime

from sqlalchemy import DateTime, Index, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.base import Base, utcnow


class ChatSession(Base):
    """A conversation. Named ChatSession to avoid confusion with SQLAlchemy's Session."""
    __tablename__ = "sessions"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    title: Mapped[str | None] = mapped_column(String(200), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=utcnow, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=utcnow, server_default=func.now())

    messages = relationship("Message", back_populates="session", cascade="all, delete-orphan", passive_deletes=True,
                            order_by="Message.seq")

    __table_args__ = (Index("ix_sessions_updated_at", "updated_at"),)
