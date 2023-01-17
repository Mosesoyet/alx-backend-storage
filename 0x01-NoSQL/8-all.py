#!/usr/bin/env python3
"""
Task 7 module
"""
import pymongo


def list_all(mongo_collection):
    """
    list all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
