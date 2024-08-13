#!/usr/bin/env python3
"""
Changes all topics of a schooll document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """Update the 'topics' field of a school document based on its name."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
