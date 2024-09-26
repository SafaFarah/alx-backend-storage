#!/usr/bin/env python3
"""
A module to fetch a webpage and cache its content using Redis.
"""

import redis
import requests
from functools import wraps
from typing import Callable

redis = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    A decorator to count how many times a particular URL is accessed.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        cache_key = f"count:{url}"
        redis.incr(cache_key)
        return method(url)
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    get content of a URL, caches it,  sets an expiration time of 10 seconds.
    Args:
        url (str): The URL to fetch the HTML content from.
    Returns:
        str: The HTML content of the page.
    """
    cached_content = redis.get(f"cache:{url}")
    if cached_content:
        return cached_content.decode('utf-8')
    response = requests.get(url)
    redis.setex(f"cache:{url}", 10, response.text)
    return response.text
