#!/usr/bin/env python3
import time
import asyncio
from 1-concurrent_coroutines import wait_n

def mesure_time(n: int, max_delay: int) -> float:
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n