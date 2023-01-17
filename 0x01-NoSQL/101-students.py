#!/usr/bin/python3
"""
Students module
"""


def top_students(mongo_collection):
    """ students
    by score"""
    return mongo_collection.aggregate([
        {
            "$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
                },
            {
                "$sort":
                {
                    "averageScore": -1
                    }
                }
            }
        ])