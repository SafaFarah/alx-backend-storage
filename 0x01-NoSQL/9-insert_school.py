#!/usr/bin/env python3
"""
Insert a new document in a collection based on kwargs
Returns new _id
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document into the collection and return the new _id."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
