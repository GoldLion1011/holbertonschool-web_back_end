#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic """
    if not mongo_collection:
        return []
    return mongo_collection.find({"topics": topic})
