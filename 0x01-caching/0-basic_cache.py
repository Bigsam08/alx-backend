#!/usr/bin/env python3
''' A basic cache class inheriting from a parent class BaseCaching '''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' basic caching class'''
    def put(self, key, item):
        ''' fix this method to make it save data to the
        dictionary cache data from the parent class
        '''
        if key is not None and item is not None:
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' use the key to get the item-data in the cache dict '''
        return self.cache_data.get(key, None)
