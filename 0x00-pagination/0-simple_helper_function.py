#!/usr/bin/env python3
""" Simple helper function """


def index_range(page, page_size):
    """Calculates the range of indexes"""

    return ((page - 1) * page_size, page * page_size)
