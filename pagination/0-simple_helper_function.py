#!/usr/bin/env python3
"""
Return the start and end index for a given page and page size.
"""


def index_range(page: int, page_size: int):
    """
    Returns the start and end index of a given page and page size.
    Args:
        page (int): The page number.
        page_size (int): The number of items per page.
    Returns:
        tuple: A tuple containing the start and end index of the page.
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
