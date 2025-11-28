#!/usr/bin/env python3
"""Module that creates a multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by multiplier

    Args:
        multiplier: the multiplier value

    Returns:
        A function that multiplies a float by multiplier
    """
    def multiply(n: float) -> float:
        """Multiply n by multiplier

        Args:
            n: number to multiply

        Returns:
            The product of n and multiplier
        """
        return n * multiplier
    return multiply
