#!/usr/bin/env python3
''' MOST RECENT USED cache class'''
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    ''' class initialization'''
    def __init__(self):
        ''' init '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' add to cache dict'''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mruKey, _ = self.cache_data.popitem(False)
                print("DISCARD:", mruKey)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ get cache data from dict"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
