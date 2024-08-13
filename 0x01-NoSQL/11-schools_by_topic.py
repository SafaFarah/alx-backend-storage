#!/usr/bin/env python3
"""
Returns list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Return a list of schools that contain the specified topic."""
    return mongo_collection.find({"topics": topic})
