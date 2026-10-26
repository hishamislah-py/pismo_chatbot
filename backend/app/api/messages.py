import json
import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
from sqlalchemy.orm import Session

from ..core.config import Settings, get_settings
from ..db.session import get_db
from ..models import Message
from ..repositories import store
from ..schemas.message import ExchangeOut, MessageCreate, MessageList, MessageOut
from ..services.assistant_service import AssistantService, get_assistant_service
from ..services.conversation import send_message, stream_exchange
from ..services.router import Router, get_router
from ..services.session_guard import SessionBusy, SessionGuard, get_session_guard
from .sessions import _not_found

BUSY_DETAIL = {"code": "session_busy",
               "message": "A message for this session is still being processed. Wait for its answer, then try again."}

router = APIRouter(prefix="/api/sessions/{session_id}/messages", tags=["messages"])


@router.get("", response_model=MessageList)
def list_messages(session_id: uuid.UUID, db: Session = Depends(get_db)):
    if store.get_session(db, session_id) is None:
        raise _not_found(session_id)
    return MessageList(session_id=session_id, messages=[MessageOut.model_validate(m) for m in store.list_messages(db, session_id)])


@router.post("", response_model=ExchangeOut, status_code=201,
             responses={409: {"description": "Another message for this session is still being processed (nothing was stored)"},
                        502: {"model": ExchangeOut, "description": "Generation failed (assistant message has status 'error')"},
                        503: {"model": ExchangeOut, "description": "Assistant not configured (e.g. missing OpenAI key)"},
                        504: {"model": ExchangeOut, "description": "Assistant timed out"}})
async def post_message(session_id: uuid.UUID, body: MessageCreate, db: Session = Depends(get_db),
                       settings: Settings = Depends(get_settings), service: AssistantService = Depends(get_assistant_service),
                       guard: SessionGuard = Depends(get_session_guard), router: Router = Depends(get_router)):
    try:
        ex = await send_message(db, settings, service, session_id, body.content, guard, router)
    except SessionBusy:
        raise HTTPException(status_code=409, detail=BUSY_DETAIL)
    if ex is None:
        raise _not_found(session_id)
    out = ExchangeOut(session_id=session_id, user_message=MessageOut.model_validate(ex.user_message),
                      assistant_message=MessageOut.model_validate(ex.assistant_message))
    return JSONResponse(status_code=ex.http_status, content=out.model_dump(mode="json"))


def _jsonable(data: dict[str, Any]) -> dict[str, Any]:
    """Messages in event data are serialised exactly as the regular API serialises them (MessageOut)."""
    def conv(v: Any) -> Any:
        if isinstance(v, Message):
            return MessageOut.model_validate(v).model_dump(mode="json")
        if isinstance(v, dict):
            return {k: conv(x) for k, x in v.items()}
        if isinstance(v, uuid.UUID):
            return str(v)
        return v
    return conv(data)


@router.post("/stream", status_code=200, response_class=StreamingResponse,
             responses={200: {"content": {"text/event-stream": {}},
                              "description": "Server-sent events: status, delta (provisional), validation, then final "
                                             "or error. See services/conversation.py stream_exchange."},
                        404: {"description": "Session not found (before the stream starts)"},
                        409: {"description": "Another message for this session is still being processed (nothing was stored)"}})
async def post_message_stream(session_id: uuid.UUID, body: MessageCreate, request: Request, db: Session = Depends(get_db),
                              settings: Settings = Depends(get_settings),
                              service: AssistantService = Depends(get_assistant_service),
                              guard: SessionGuard = Depends(get_session_guard),
                              router: Router = Depends(get_router)):
    """Streaming variant of POST /messages. Failures that are known before the stream starts keep their HTTP status
    (404, 409, 422); after it starts, every outcome is an event. The answer text in `delta` events is provisional; only
    the `final` event carries the validated, stored answer."""
    exists = store.get_session(db, session_id) is not None
    db.rollback()                                   # end the read-only check's transaction before streaming
    if not exists:
        raise _not_found(session_id)
    if guard.is_busy(session_id):                   # the atomic acquisition happens inside the stream
        raise HTTPException(status_code=409, detail=BUSY_DETAIL)
    request_id = str(uuid.uuid4())

    async def events():
        seq = 0
        async for event, data in stream_exchange(db, settings, service, session_id, body.content, guard,
                                                 is_disconnected=request.is_disconnected, router=router):
            if event == "comment":
                yield ": keep-alive\n\n"
                continue
            seq += 1
            payload = json.dumps({"request_id": request_id, **_jsonable(data)}, ensure_ascii=False, separators=(",", ":"))
            yield f"id: {seq}\nevent: {event}\ndata: {payload}\n\n"

    return StreamingResponse(events(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})
