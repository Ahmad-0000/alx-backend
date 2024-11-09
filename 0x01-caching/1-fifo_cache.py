#!/usr/bin/env python3
"""
FIFO Cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching class"""
    def __init__(self):
        """Initializing an object"""
        super().__init__()
        self.caching_queue = []

    def put(self, key, item):
        """Caching data"""
        if not key or not item:
            return
        if len(self.caching_queue) > BaseCaching.MAX_ITEMS:
            deleted = self.caching_queue[0]
            del self.caching_queue[0]
            print(f"DISCARD: {deleted}")
        self.caching_queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Getting an item from a cache"""
        return self.cache_data.get(key)
