#!/usr/bin/env python3
"""
a coroutine that executes async_comprehension four times
in parallel using asyncio.gather,
measures the total runtime and returns it
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    executes async_comprehension four times,
    and measures the total runtime and returns it
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
