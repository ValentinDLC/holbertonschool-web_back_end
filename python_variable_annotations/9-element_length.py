#!/usr/bin/env python3
"""Module that returns a list of tuples with elements and their lengths"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element and its length

    Args:
        lst: an iterable of sequences

    Returns:
        A list of tuples with each sequence and its length
    """
    return [(i, len(i)) for i in lst]
