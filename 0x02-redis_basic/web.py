#!/usr/bin/env python3
"""
A module to fetch a webpage and cache its content using Redis.
"""

import redis
import requests
from functools import wraps
from typing import Callable


def count_requests(method: Callable) -> Callable:
    """
    A decorator to count how many times a particular URL is accessed.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """The wrapper function for caching the output.
        """
        r = redis.Redis()
        r.incr(f'count:{url}')
        cached_page = r.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = method(url)
        r.set(f'{url}', response, 10)
        return response
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
    return requests.get(url).text
