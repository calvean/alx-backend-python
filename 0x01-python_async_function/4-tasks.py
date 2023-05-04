#!/usr/bin/env python3
""" task_wait_n module """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutines at the same time with async
    Args:
        n (int) - number to spawn wait_random
        max_delay (int) - maximum delay
    Return:
        delay (list) - lis of list of all the delays  in accending order
    """
    delays = []
    for i in range(n):
        task = task_wait_random(max_delay)
        await task
        delay = task.result()
        delays.append(delay)
    return delays
