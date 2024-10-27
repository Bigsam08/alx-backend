#!/usr/bin/env python3
''' function named index_range taking two int params
page and page_size returning a tuple of size'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' return pagination parameters(start and end)
    @page: current page
    @page_size: total number of list in page '''
    startIndex = page * page_size
    endPage = startIndex - page_size
    return endPage, startIndex
