#!/usr/bin/env python3
"""A module containing a caching class that uses the FIFO algorithm"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class that inherits from BaseCaching and caches with FIFO algorithm"""

    def __init__(self):
        """Initialize the class instance"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add a key/value pair to the cache"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= self.MAX_ITEMS:
                popped = self.queue.pop(0)
                del self.cache_data[popped]
                print('DISCARD:', popped)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the given key"""
        return self.cache_data.get(key)
