import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ActivityOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    created_at: datetime
    session_id: uuid.UUID | None
    event: str
    status: str
    http_status: int
    duration_ms: int
    evidence_count: int | None
    citation_count: int | None
    model: str | None
    error_kind: str | None


class ActivityList(BaseModel):
    activity: list[ActivityOut]
