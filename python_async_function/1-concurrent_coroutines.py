#!/usr/bin/env python3
"""Module with async routine that spawns wait_random n times"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay

    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay for wait_random

    Returns:
        List of all delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []
    for coro in asyncio.as_completed(tasks):
        res = await coro
        results.append(res)
    return results
