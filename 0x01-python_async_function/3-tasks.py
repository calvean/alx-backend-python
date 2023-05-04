#!/usr/bin/env python3
""" task_wait_random module """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function that takes an integer max_delay and returns a asyncio
    Args:
        max_delay (int) - maximum delay
    Return:
        asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
