#!/usr/bin/env python3
"""Module that creates a tuple from a string and the square of a number"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with a string and the square of a number

    Args:
        k: string key
        v: int or float value

    Returns:
        A tuple with k and the square of v as a float
    """
    return (k, float(v ** 2))
