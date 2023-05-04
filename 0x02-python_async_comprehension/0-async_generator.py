#!/usr/bin/env python3
""" async_generator module """
import random
from asyncio import sleep
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async generator that produce a random number
        for 10 iterations, after every 10s
    """
    for i in range(10):
        await sleep(1)
        yield 10 * random()
