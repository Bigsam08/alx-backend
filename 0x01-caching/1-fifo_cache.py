#!/usr/bin/env python3
'''First in FIrst Out class '''
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    ''' create class '''
    def __init__(self):
        ''' initialization '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' add data to cache'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstKey, _ = self.cache_data.popitem(False)
            print("DISCARD:", firstKey)

    def get(self, key):
        ''' return item searched by key'''
        return self.cache_data.get(key, None)
