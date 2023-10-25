#!/usr/bin/env python3
"""A module containing a caching class that uses the LIFO algorithm"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class that inherits from BaseCaching and caches with LIFO algorithm"""
    def __init__(self):
        """Initialize the class instance"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """A method that adds key/value pair to the cache"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.stack.remove(key)
                self.stack.append(key)
                return
            if len(self.cache_data) >= self.MAX_ITEMS:
                popped = self.stack.pop()
                del self.cache_data[popped]
                print('DISCARD:', popped)
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """A method that returns the value associated with the given key"""
        return self.cache_data.get(key)
