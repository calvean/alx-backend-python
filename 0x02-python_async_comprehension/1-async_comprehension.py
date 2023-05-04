#!/usr/bin/env python3
""" async_comprehension module """
import asyncio
from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async function that collects 10 random numbers
     then return the 10 random numbers
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers
