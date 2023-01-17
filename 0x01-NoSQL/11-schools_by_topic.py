#!/usr/bin/env python3
"""
task 11 modules
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    find topic
    """
    return mongo_collection.find({"topics": topic})
