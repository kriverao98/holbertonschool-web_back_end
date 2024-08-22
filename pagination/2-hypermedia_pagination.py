#!/usr/bin/env python3
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.
        Args:
            page (int): The page number to retrieve. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.
        Returns:
            List[List]: The data for the specified page.
        Raises:
            AssertionError: If `page` or `page_size` is not a positive integer.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        if page > total_pages:
            return []

        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return dataset[start_index:end_index]


    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieves a dictionary containing hypermedia pagination information.
        Args:
            page (int): The current page number (default is 1).
            page_size (int): The number of items per page (default is 10).
        Returns:
            dict: A dictionary containing the following keys:
                - 'page_size': The number of items in the current page.
                - 'page': The current page number.
                - 'data': The dataset for the current page.
                - 'next_page': The next page number, or None if there
                is no next page.
                - 'prev_page': The previous page number, or None if there is no
                previous page.
                - 'total_pages': The total number of pages.
        """

        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(dataset),
            'page': page,
            'data': dataset,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
