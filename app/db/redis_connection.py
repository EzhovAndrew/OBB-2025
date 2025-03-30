import redis.asyncio as redis
from settings import settings


class RedisConnection:
    """Proxy operations with Redis."""

    def __init__(self):
        self.connection = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            decode_responses=True,
        )

    async def add_value_to_set(self, key: str, value: str) -> int:
        """Add value to set."""
        return await self.connection.sadd(key, value)

    async def get_set_members(self, key: str) -> list:
        """Get set members."""
        return await self.connection.smembers(key)

    async def delete_value_from_set(self, key: str, value: str) -> int:
        """Delete value from set."""
        return await self.connection.srem(key, value)


redis_connection = RedisConnection()
