#!/usr/bin/env python3
""" measure_runtime module """
import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension 4 times in parallel
     and measure the total runtime
    """
    start_time = perf_counter()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = perf_counter()
    total_runtime = end_time - start_time

    return total_runtime
