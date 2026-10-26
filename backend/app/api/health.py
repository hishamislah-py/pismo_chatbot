from fastapi import APIRouter, Depends

from ..db.session import database_status
from ..services.assistant_service import AssistantService, get_assistant_service

router = APIRouter(tags=["health"])


@router.get("/api/health")
def health(service: AssistantService = Depends(get_assistant_service)):
    """Application health. Reports component states only - no URLs, paths, credentials or configuration values.
    index.chunk_set_hash identifies the knowledge-base index held in memory (null until it is loaded; never loads it)."""
    db = database_status()
    assistant = "loaded" if service.loaded else ("error" if service.load_error else "not_loaded")
    return {"status": "ok" if db == "ok" else "degraded", "app": "ok", "database": db, "assistant": assistant,
            "index": {"chunk_set_hash": service.index_version}}
