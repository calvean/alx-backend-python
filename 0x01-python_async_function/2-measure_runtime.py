#!/usr/bin/env python3
""" measure_runtime Module """
import asyncio
import random
from typing import List
import time

wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the runtime
    Args:
        n (int) - number to spawn wait_random
        max_delay (int) - maximum delay
    Return:
        runtime (float)
    """
    start_time = time.monotonic()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.monotonic()
    total_time = end_time - start_time
    return total_time / n
