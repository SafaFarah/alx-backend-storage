#!/usr/bin/env python3
"""
module contains a function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """Return a list of students sorted by their average score.
    Args:
        mongo_collection: The pymongo collection object.
    Returns:
        A list of dictionaries representing students, each with an
        'averageScore' key, sorted by 'averageScore' in descending order.
    """
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    return mongo_collection.aggregate(pipeline)
