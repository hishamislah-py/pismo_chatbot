import uuid

from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session

from ..db.session import get_db
from ..repositories import store
from ..schemas.session import SessionCreate, SessionList, SessionOut

router = APIRouter(prefix="/api/sessions", tags=["sessions"])


def _not_found(session_id: uuid.UUID) -> HTTPException:
    return HTTPException(status_code=404, detail={"code": "session_not_found", "message": f"session {session_id} not found"})


@router.post("", response_model=SessionOut, status_code=201)
def create_session(body: SessionCreate | None = None, db: Session = Depends(get_db)):
    s = store.create_session(db, title=(body.title.strip() or None) if body and body.title else None)
    db.commit()
    return SessionOut.model_validate(s).model_copy(update={"message_count": 0})


@router.get("", response_model=SessionList)
def list_sessions(limit: int = Query(default=50, ge=1, le=200), db: Session = Depends(get_db)):
    return SessionList(sessions=[SessionOut.model_validate(s).model_copy(update={"message_count": n})
                                 for s, n in store.list_sessions(db, limit)])


@router.get("/{session_id}", response_model=SessionOut)
def get_session(session_id: uuid.UUID, db: Session = Depends(get_db)):
    s = store.get_session(db, session_id)
    if s is None:
        raise _not_found(session_id)
    return SessionOut.model_validate(s).model_copy(update={"message_count": store.count_messages(db, session_id)})


@router.delete("/{session_id}", status_code=204)
def delete_session(session_id: uuid.UUID, db: Session = Depends(get_db)):
    if not store.delete_session(db, session_id):
        raise _not_found(session_id)
    db.commit()
    return Response(status_code=204)
