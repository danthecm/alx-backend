#!/usr/bin/env python3
"""A module containing a caching class that uses the LRU algorithm"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A class that inherits from BaseCaching and caches with LRU algorithm"""
    def __init__(self):
        """Initialize the class instance"""
        super().__init__()
        self.key_tracker = {}

    def put(self, key, item):
        """A method that adds key/value pair to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the LRU item and remove it
                lru_key = min(self.key_tracker, key=self.key_tracker.get)
                print(f"DISCARD: {lru_key}")
                del self.key_tracker[lru_key]
                del self.cache_data[lru_key]
            if not self.key_tracker.get(key):
                self.key_tracker[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        """A method that retrieves an item from the cache"""
        if key in self.cache_data:
            self.key_tracker[key] += 1
            return self.cache_data[key]
        return None
