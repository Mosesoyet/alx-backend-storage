#!/usr/bin/env python3
"""
task 10 modules
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update rows
    """
    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topic": topics}}
            )
