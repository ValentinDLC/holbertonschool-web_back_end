#!/usr/bin/env python3
from 0-async_generator import async_generator
from typing import List

async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator using async comprehension."""
    return [i async for i in async_generator()]