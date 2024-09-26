#!/usr/bin/env python3
"""
This module contains a Cache class to interact with Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
import functools


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of times a method is called.
    Args:
        method (Callable): The method to be decorated.
    Returns:
        Callable: The wrapped method with a call counter.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Wrapper function that increments count each time the method is called.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the input and output history of a method.
    Args:
        method (Callable): The method to decorate.
    Returns:
        Callable: The decorated method with call history tracking.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ Generate keys for inputs and outputs"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    Replay the history of a particular method,display  all its inputs, outputs.
    Args:
        method: The method to replay the history of.
    """
    redis_client = method.__self__._redis
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    inputs = redis_client.lrange(input_key, 0, -1)
    outputs = redis_client.lrange(output_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_, output in zip(inputs, outputs):
        input_str = input_.decode('utf-8')
        output_str = output.decode('utf-8')
        print(f"{method.__qualname__}(*{input_str}) -> {output_str}")


class Cache:
    """Cache class to store and retrieve data from Redis."""
    def __init__(self):
        """Initialize Redis client and flush any existing data."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
