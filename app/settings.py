from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App settings."""

    redis_host: str = Field(..., alias="REDIS_HOST")
    redis_port: int = Field(..., alias="REDIS_PORT")
    redis_db: int = Field(..., alias="REDIS_DB")


settings = Settings()
