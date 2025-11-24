#!/usr/bin/env python3
import asyncio
import time
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """Run async_comprehension 4 times in parallel and return total runtime."""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.time()
    return end - start