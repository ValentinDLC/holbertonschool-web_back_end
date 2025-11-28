#!/usr/bin/env python3
"""Module with async routine that spawns task_wait_random n times"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with the specified max_delay

    Args:
        n: number of times to spawn task_wait_random
        max_delay: maximum delay for task_wait_random

    Returns:
        List of all delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        res = await task
        results.append(res)
    return results
