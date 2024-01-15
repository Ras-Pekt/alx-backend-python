#!/usr/bin/env python3
"""an async routine called wait_n
that takes in 2 int arguments: n and max_delay,
spawns wait_random n times with the specified max_delay,
and returns the list of all the delays in ascending order
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in 2 int arguments,
    spawns wait_random n times with the specified max_delay,
    returns the list of all the delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays_lists = [await delay for delay in asyncio.as_completed(tasks)]

    return delays_lists
