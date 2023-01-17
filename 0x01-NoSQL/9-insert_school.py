#!/usr/bin/env python3
"""
task 9 modules
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert in school
    """
    return mongo_collection.insert_one(kwargs).inserted_id
