from typing import Annotated

from db.db import SessionRepository
from fastapi import APIRouter, Depends, Path, Query
from rest.dependencies import get_session_repository
from rest.models import Session, User, UserSessions

router = APIRouter(prefix="/sessions")


@router.get("")
async def get_sessions(
    user_id: Annotated[int, Query(ge=1)],
    session_repository: Annotated[SessionRepository, Depends(get_session_repository)],
) -> UserSessions:
    """Get all sessions."""
    sessions = await session_repository.get_user_sessions(user_id)
    return UserSessions(user_id=user_id, session_ids=sessions)


@router.post("")
async def create_session(
    user: User,
    session_repository: Annotated[SessionRepository, Depends(get_session_repository)],
) -> Session:
    """Create session."""
    session_id = await session_repository.create_session(user.id)
    return Session(user_id=user.id, session_id=session_id)


@router.delete("", status_code=204)
async def delete_session(
    user_id: Annotated[int, Query(ge=1)],
    session_id: Annotated[str, Query(min_length=1)],
    session_repository: Annotated[SessionRepository, Depends(get_session_repository)],
):
    """Delete session."""
    await session_repository.delete_session(user_id=user_id, session_id=session_id)
