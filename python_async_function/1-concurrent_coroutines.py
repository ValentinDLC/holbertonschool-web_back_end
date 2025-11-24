#!/usr/bin/env python3
import asyncio 
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []
    for coro in asyncio.as_completed(tasks):
        res = await coro
        results.append(res)
    return results