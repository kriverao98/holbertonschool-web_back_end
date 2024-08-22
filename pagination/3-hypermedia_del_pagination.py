#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int]
                        = 0, page_size: int = 10) -> Dict:
        """
        Retrieves a dictionary containing hypermedia pagination information.
        Args:
            index (Optional[int]): The index of the starting item of the page.
            page_size (int): The number of items per page.
        Returns:
            dict: A dictionary containing the following keys:
                - 'index': The starting index of the current page.
                - 'next_index': The index to query for the next page.
                - 'page_size': The number of items per page.
                - 'data': The dataset for the current page.
        """
        assert isinstance(index, int) and index >= 0

        indexed_dataset = self.indexed_dataset()

        page_data: List[List] = []
        while len(page_data) < page_size and index in indexed_dataset:
            page_data.append(indexed_dataset[index])
            index += 1

        next_index = index

        return {
            'index': index - len(page_data),
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data
        }
