#!/usr/bin/env python3
"""
LRU caching
"""
from base_caching import BaseCaching


def LRUCache(BaseCaching):
    """LRU caching class"""
    def __init__(self):
        """Initializing an object"""
        super().__init__()
        self.lru_queue = []

    def put(self, key, item):
        """Caching an item"""
        if not key or not item:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            deleted = self.lru_queue.pop()
            del self.cache_data[deleted]
            print(f"DISCARD: {deleted}")
        self.cache_data[key] = item

    def get(self, key):
        """Getting an item from the list"""
        if key and key in self.lru_queue:
            i = self.lru_queue.index(key) + 1
            self.lru_queue.append(key)
            del self.lru_queue[i]
        return self.cache_data.get(key)
