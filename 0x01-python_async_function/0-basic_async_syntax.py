#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument, max_delay
waits for a random delay between 0 and max_delay seconds
and eventually returns it
"""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> List[float]:
    """
    takes in an integer argument
    waits for a random delay
    and eventually returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
