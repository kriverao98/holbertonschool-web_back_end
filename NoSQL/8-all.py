#!/usr/bin/env python3
""" 8-all """

def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
        list: A list of documents in the collection. Returns an empty list if no documents are found.
    """
    return list(mongo_collection.find())
