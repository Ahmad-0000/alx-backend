#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary
        """
        assert index >= 0
        dataset = self.indexed_dataset()
        assert index < len(dataset)
        retval = {}
        data = []
        i = 0
        temp = index
        while i < (page_size + 1):
            if dataset.get(temp):
                data.append((temp, dataset[temp]))
                i += 1
                temp += 1
            else:
                temp += 1
        retval["index"] = index
        retval["data"] = [_[1] for _ in data][:-1]
        retval["page_size"] = page_size
        retval["next_index"] = data[-1][0]
        return retval
