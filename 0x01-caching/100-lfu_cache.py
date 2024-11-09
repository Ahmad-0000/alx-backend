#!/usr/bin/env python3
"""
LFU caching
"""
from base_caching import BaseCaching
from datetime import datetime


class LFUCache(BaseCaching):
    """LFU caching class"""
    def __init__(self):
        """Initializing an object"""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Caching an item"""
        if not key or not item:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            frequencies = [i["fu"] for i in self.frequency.values()]
            lfu = min(frequencies)
            if frequencies.count(lfu) > 1:
                atimes = [i["ru"] for i in self.frequency.values()]
                lru = min(atimes)
                for k, v in self.frequency.items():
                    if self.frequency[k]["fu"] == lfu and\
                            self.frequency[k]["ru"] == lru:
                        del self.frequency[k]
                        del self.cache_data[k]
                        print(f"DISCARD: {k}")
                        break
            else:
                for k in self.frequency.keys():
                    if self.frequency[k]["fu"] == lfu:
                        del self.frequency[k]
                        del self.cache_data[k]
                        print(f"DISCARD: {k}")
                        break
        self.cache_data[key] = item
        self.frequency[key] = {"fu": 0, "ru": "0"}

    def get(self, key):
        """Getting an item from the list"""
        if key in self.cache_data:
            self.frequency[key]['fu'] += 1
            self.frequency[key]['ru'] = str(datetime.now())
        return self.cache_data.get(key)
