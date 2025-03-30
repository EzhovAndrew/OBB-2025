from uuid import uuid4

from db.redis_connection import redis_connection


class SessionRepository:
    """Session repository."""

    def __init__(self):
        self.db_connection = redis_connection

    async def get_user_sessions(self, user_id: int) -> list[str]:
        """Get user sessions."""
        return await self.db_connection.get_set_members(f"user:{user_id}:sessions")

    async def create_session(self, user_id: int) -> str:
        """Create session."""
        session_id = str(uuid4())
        await self.db_connection.add_value_to_set(f"user:{user_id}:sessions", session_id)
        return session_id

    async def delete_session(self, user_id: int, session_id: str) -> None:
        """Delete session."""
        await self.db_connection.delete_value_from_set(f"user:{user_id}:sessions", session_id)
