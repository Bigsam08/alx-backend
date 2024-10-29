#!/usr/bin/env python3
''' last in first out class'''
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    ''' initialization '''
    def __init__(self):
        ''' slef init'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' add data to cache '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lastKey, _ = self.cache_data.popitem(True)
                print("DISCARD:", lastKey)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        ''' get item from data cache dictionary'''
        return self.cache_data.get(key, None)
