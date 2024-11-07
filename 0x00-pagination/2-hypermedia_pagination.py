#!/usr/bin/env python3
"""
2nd task's solution
"""
import csv
import math
from typing import List, Tuple, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Getting a page in a HATEOAS style"""
        retval = {}
        try:
            current_page = self.get_page(page, page_size)
        except AssertionError:
            return {}
        start_index, end_index = index_range(page, page_size)
        retval["page_size"] = len(current_page)
        retval["page"] = page
        retval["data"] = current_page
        try:
            self.__dataset[end_index + page_size - 1]
            retval["next_page"] = page + 1
        except IndexError:
            retval["next_page"] = None
        if (start_index - page_size) > 0:
            retval["prev_page"] = page - 1
        else:
            retval["prev_page"] = None
        retval["total_pages"] = len(self.__dataset) // page_size
        return retval
