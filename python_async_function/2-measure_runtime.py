#!/usr/bin/env python3
"""Module that measures the runtime of wait_n"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)

    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay for wait_random

    Returns:
        Average time per coroutine (total_time / n)
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
