#!/usr/bin/env python3
"""
Simple pagination with Server class
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination parameters.
    
    Args:
        page: The page number (1-indexed)
        page_size: The number of items per page
    
    Returns:
        A tuple containing (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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
        """
        Get a page of the dataset.
        
        Args:
            page: The page number (1-indexed), default 1
            page_size: The number of items per page, default 10
        
        Returns:
            A list of rows for the requested page, or empty list if out of range
        """
        # Verify that both arguments are integers greater than 0
        assert isinstance(page, int) and page > 0, \
            "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be an integer greater than 0"
        
        # Get the dataset
        data = self.dataset()
        
        # Calculate the start and end indexes
        start_index, end_index = index_range(page, page_size)
        
        # Return the appropriate page or empty list if out of range
        if start_index >= len(data):
            return []
        
        return data[start_index:end_index]
    