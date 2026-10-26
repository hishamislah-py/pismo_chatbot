import uuid
from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..core.config import get_settings


class MessageCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    content: str = Field(min_length=1, description="The user's question")

    @field_validator("content")
    @classmethod
    def _check(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("content must not be blank")
        limit = get_settings().max_question_chars
        if len(v) > limit:
            raise ValueError(f"content exceeds {limit} characters")
        return v


class CitationSource(BaseModel):
    path: str
    url: str


class Citation(BaseModel):
    """A validated citation exactly as returned by the pipeline (no fields are invented by the backend)."""
    label: str
    ku_id: str
    title: str
    section: str
    chunk_id: str
    origin: str | None = None
    sources: list[CitationSource]


class MessageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    session_id: uuid.UUID
    seq: int
    role: Literal["user", "assistant"]
    content: str
    status: str | None = None
    citations: list[Citation] | None = None
    details: dict[str, Any] | None = None
    created_at: datetime


class MessageList(BaseModel):
    session_id: uuid.UUID
    messages: list[MessageOut]


class ExchangeOut(BaseModel):
    """Response of POST /api/sessions/{id}/messages."""
    session_id: uuid.UUID
    user_message: MessageOut
    assistant_message: MessageOut
