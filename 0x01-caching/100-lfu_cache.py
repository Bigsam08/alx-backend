#!/usr/bin/env python3
''' LEAST FREQUENTLY USED'''
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    ''' Initialiization of class'''
    def __init__(self):
        ''' class inheritance'''
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mruKey):
        ''' reorder the items in the cache from most frequently used'''
        max_pos = []
        mru_freq = 0, mru_pos = 0, ins_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mruKey:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_pos) == 0:
                max_pos.append(i)
            elif key_freq[1] < self.keys_freq[max_pos[-1]][1]:
                max_pos.append(i)
        max_pos.reverse()
        for pos in max_pos:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mruKey, mru_freq])

    def put(self, key, item):
        ''' add data to data cache dict'''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfuKey, _ = self.keys_freq[-1]
                self.cache_data.pop(lfuKey)
                self.keys_freq.pop()
                print("DISCARD:", lfuKey)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        ''' get data from cache dict'''
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
