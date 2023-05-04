#!/usr/bin/env python3
""" Wait Random Module """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine
    Args:
        max_delay (int) - max delay time
    Return:
        delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
