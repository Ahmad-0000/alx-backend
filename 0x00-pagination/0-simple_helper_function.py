#!/usr/bin/env python3
"""
1s task's solution
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end indexes"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
