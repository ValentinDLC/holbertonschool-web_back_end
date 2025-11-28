#!/usr/bin/env python3
"""Module that sums a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum all floats in a list

    Args:
        input_list: list of float numbers

    Returns:
        The sum of all floats in the list
    """
    return sum(input_list)
