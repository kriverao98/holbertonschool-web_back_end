#!/usr/bin/env python3
from async_comprehension import async_comprehension
import asyncio
import time


async def measure_runtime() -> float:
    """
    Measure the runtime of the async_comprehension function.

    Returns:
        float: The total runtime in seconds.

    Comment:
        This function uses asyncio.gather
        to execute the async_comprehension function four
        times and measures the total runtime.
    """

    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    end_time = time.time()

    total_time = end_time - start_time
    return total_time
