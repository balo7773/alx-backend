#!/usr/bin/env python3
"""Module function"""
import csv
import math
from typing import List


def index_range(page, page_size):
    "index Method"
    start = int(page - 1) * page_size
    end = start + page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the current page"""
        assert isinstance(page_size, int)
        assert isinstance(page, int)
        assert page > 0
        assert page_size > 0
        self.dataset()
        start, stop = index_range(page, page_size)

        try:
            return self.__dataset[start:stop]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the current page"""
        assert isinstance(page_size, int)
        assert isinstance(page, int)
        assert page > 0
        assert page_size > 0
        data = self.dataset()
        total_pages = (len(data) + page_size - 1) // page_size

        obj = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": None,
            "prev_page": None,
            "total_pages": total_pages,
        }

        if page > 1:
            obj["prev_page"] = page - 1

        if page < total_pages:
            obj["next_page"] = page + 1

        return obj