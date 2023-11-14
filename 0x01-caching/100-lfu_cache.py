#!/usr/bin/env python3
"""A module containing a class LFUCache"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class that implements the LFU caching system"""

    def __init__(self):
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discard = min(self.freq, key=self.freq.get)
                del self.cache_data[discard]
                del self.freq[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.freq[key] = 1

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        return self.cache_data[key]
