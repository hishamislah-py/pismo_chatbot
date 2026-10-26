from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ..db.session import get_db
from ..repositories import store
from ..schemas.activity import ActivityList, ActivityOut

router = APIRouter(tags=["activity"])


@router.get("/api/activity", response_model=ActivityList)
def list_activity(limit: int = Query(default=50, ge=1, le=200), db: Session = Depends(get_db)):
    """Recent assistant requests: timestamp, session, status, duration, evidence/citation counts. No message text."""
    return ActivityList(activity=[ActivityOut.model_validate(a) for a in store.list_activity(db, limit)])
