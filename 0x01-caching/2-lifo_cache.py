#!/usr/bin/env python3
"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching class"""
    def __init__(self):
        """Initializing an object"""
        super().__init__()
        self.caching_stack = []

    def put(self, key, item):
        """Caching data"""
        if not key or not item:
            return
        if len(self.caching_stack) == BaseCaching.MAX_ITEMS:
            deleted = self.caching_stack.pop()
            del self.cache_data[deleted]
            print(f"DISCARD: {deleted}")
        self.caching_stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Getting an item from a cache"""
        return self.cache_data.get(key)
