from db.db import SessionRepository


def get_session_repository() -> SessionRepository:
    """Get session repository."""
    return SessionRepository()
