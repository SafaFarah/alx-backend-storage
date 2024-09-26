#!/usr/bin/env python3
"""
A module to fetch a webpage and cache its content using Redis.
"""

import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    A decorator to count how many times a particular URL is accessed.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        cache_key = f"count:{url}"
        r.incr(cache_key)
        return method(url)
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Get content of a URL, caches it, and sets an expiration time of 10 seconds.
    Args:
        url (str): The URL to fetch the HTML content from.
    Returns:
        str: The HTML content of the page.
    """
    cache_key = f"cache:{url}"
    cached_content = r.get(cache_key)
    if cached_content:
        return cached_content.decode('utf-8')
    r.setex(cache_key, 10, response.text)
    return response.text
