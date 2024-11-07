#!/usr/bin/env python3
"""
2nd task's solution
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end indexes"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
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
        """Getting a page"""
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        if self.__dataset is None:
            self.dataset()
        start_index, end_index = index_range(page, page_size)
        try:
            self.__dataset[end_index]
            self.__dataset[start_index]
            return self.__dataset[start_index:end_index]
        except IndexError:
            return []
