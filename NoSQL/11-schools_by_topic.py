#!/usr/bin/env python3
""" 11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """
    Return a list of school documents that contain a
    specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The pymongo collection object.
        topic (str): The topic to search for in the schools'
        topics.

    Returns:
        list: A list of school documents where the 'topics'
        field contains the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
