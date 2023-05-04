#!/usr/bin/env python3
""" Concurrent_coroutines Module """

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutines at the same time with async
    Args:
        n (int) - number to spawn wait_random
        max_delay (int) - maximum delay
    Return:
        delay (list) - lis of list of all the delays  in accending order
    """
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
