#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The pymongo collection object.
        **kwargs: Key-value pairs to be inserted as fields
        in the document.

    Returns:
        ObjectId: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
