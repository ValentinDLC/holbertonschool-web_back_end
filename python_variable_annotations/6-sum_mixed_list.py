#!/usr/bin/env python3
"""Module that sums a mixed list of integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum all integers and floats in a list

    Args:
        mxd_lst: list of integers and floats

    Returns:
        The sum of all numbers in the list as a float
    """
    return sum(mxd_lst)
