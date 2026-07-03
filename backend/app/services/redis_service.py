import json
import logging
import os

import redis
from redis.exceptions import RedisError

logger = logging.getLogger(__name__)


class RedisService:
    """
    Singleton-style Redis connection manager.

    Responsibilities:
    - Manage Redis connection
    - Health checks
    - Graceful fallback
    - Basic cache operations
    """

    def __init__(self):
        self.enabled = False
        self.client = None

        host = os.getenv("REDIS_HOST", "localhost")
        port = int(os.getenv("REDIS_PORT", 6379))
        db = int(os.getenv("REDIS_DB", 0))

        try:
            self.client = redis.Redis(
                host=host,
                port=port,
                db=db,
                decode_responses=True,
            )

            self.client.ping()

            self.enabled = True

            logger.info("✅ Connected to Redis successfully.")

        except RedisError as e:
            self.enabled = False
            self.client = None

            logger.warning(
                f"Redis unavailable. Falling back to SQLite only. ({e})"
            )

    def is_available(self) -> bool:
        """
        Returns True if Redis is connected.
        """
        return self.enabled

    def health_check(self) -> bool:
        """
        Performs a Redis ping.
        """
        if not self.client:
            return False

        try:
            self.client.ping()
            return True

        except RedisError:
            return False

    def get(self, key):
        """
        Read cached JSON.
        """
        if not self.enabled:
            return None

        try:
            value = self.client.get(key)

            if value is not None:
                logger.info(f"Redis HIT: {key}")
            else:
                logger.info(f"Redis MISS: {key}")

            logger.info(f"Redis SET: {key}")
            return json.loads(value)
            
        except RedisError:
            return None

    def set(self, key, value, ttl=60):
        """
        Store JSON in cache.
        """
        if not self.enabled:
            return

        try:
            self.client.setex(
                key,
                ttl,
                json.dumps(value),
            )
            logger.info(f"Redis SET: {key}")
        except RedisError:
            logger.warning("Redis SET failed.")

    def delete(self, *keys):
        """
        Delete cache keys.
        """
        if not self.enabled:
            return

        try:
            self.client.delete(*keys)

        except RedisError:
            logger.warning("Redis DELETE failed.")


redis_service = RedisService()