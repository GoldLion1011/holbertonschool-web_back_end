#!/usr/bin/env python3
""" MRU Caching """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Put in cache """
        if key and item:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.keys.pop()
                del self.cache_data[discard]
                print("DISCARD:", discard)
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get from cache """
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
