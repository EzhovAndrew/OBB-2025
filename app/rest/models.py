from pydantic import BaseModel, Field


class User(BaseModel):
    """User model."""

    id: int = Field(..., ge=1, alias="user_id")


class Session(BaseModel):
    """Session model."""

    session_id: str = Field(..., min_length=1)
    user_id: int = Field(..., ge=1)


class UserSessions(BaseModel):
    """User sessions model."""

    user_id: int = Field(..., ge=1)
    session_ids: list[str] = Field(default_factory=list)
