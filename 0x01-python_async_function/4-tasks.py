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
    tasks: List[float] = []
    all_tasks: List[float] = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(tasks):
        result = await delay
        all_tasks.append(result)
    return all_tasks
