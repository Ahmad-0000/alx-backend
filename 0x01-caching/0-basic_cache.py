#!/usr/bin/env python3
"""
Unlimited caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Unlimited caching class"""
    def put(self, key, item):
        """Caching an item"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Getting back an item"""
        return self.cache_data.get(key)
