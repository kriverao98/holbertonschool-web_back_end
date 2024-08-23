#!/usr/bin/env python3
""" 10-update_topics """


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document in the MongoDB
    collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The pymongo collection object.
        name (str): The name of the school document to update.
        topics (list of str): The list of topics to update
        in the school document.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
