#!/usr/bin/env python3
""" async_generator module """
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Async generator that produce a random number
        for 10 iterations, after every 10s
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
