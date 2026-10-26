import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SessionCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str | None = Field(default=None, max_length=200, description="Optional; derived from the first question if omitted")


class SessionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    title: str | None
    created_at: datetime
    updated_at: datetime
    message_count: int = 0


class SessionList(BaseModel):
    sessions: list[SessionOut]
