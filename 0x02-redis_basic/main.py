#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

# Store different types of data
cache.store("foo")
cache.store("bar")
cache.store(42)

# Replay the call history for the store method
cache.replay(cache.store)
