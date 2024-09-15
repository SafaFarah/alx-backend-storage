#!/usr/bin/env python3
"""
This module contains a Cache class to interact with Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Cache class to store and retrieve data from Redis."""
    def __init__(self):
        """Initialize Redis client and flush any existing data."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the generated key.
        Args:
            data (Union[str, bytes, int, float]): The data to be stored.
        Returns:
            str: The generated random key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a UTF-8 string from Redis.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.
        """
        return self.get(key, int)
