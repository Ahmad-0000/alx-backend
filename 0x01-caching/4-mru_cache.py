#!/usr/bin/env python3
"""
MRU caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching class"""
    def __init__(self):
        """Initializing an object"""
        super().__init__()
        self.mru_stack = []

    def put(self, key, item):
        """Caching an item"""
        if not key or not item:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            deleted = self.mru_stack.pop()
            del self.cache_data[deleted]
            print(f"DISCARD: {deleted}")
        self.cache_data[key] = item
        self.mru_stack.append(key)

    def get(self, key):
        """Getting an item from the cache"""
        if key in self.mru_stack:
            self.mru_stack.append(key)
            del self.mru_stack[self.mru_stack.index(key)]
        return self.cache_data.get(key)
