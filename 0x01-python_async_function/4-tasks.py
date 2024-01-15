#!/usr/bin/env python3
"""
an altered wait_n to a new function task_wait_n,
that calls task_wait_random function
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    calls task_wait_random function
    """

    """
    task = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]
    delays_lists = [await delay for delay in asyncio.as_completed(task)]

    return delays_lists
    """

    tasks = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(tasks)
