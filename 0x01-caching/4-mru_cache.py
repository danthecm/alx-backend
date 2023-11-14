#!/usr/bin/env python3
"""A module containing a class MRUCache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that implements MRU caching system"""

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.stack.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discard = self.stack.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))
        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.stack.remove(key)
        self.stack.append(key)
        return self.cache_data[key]
