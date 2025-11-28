#!/usr/bin/env python3
"""Module with an asynchronous coroutine that waits for a random delay"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds

    Args:
        max_delay: maximum delay in seconds (default: 10)

    Returns:
        The actual delay waited as a float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
