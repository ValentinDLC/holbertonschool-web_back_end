#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


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
