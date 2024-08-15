#!/usr/bin/env python3
"""Testing async functions"""
from basic_async_syntax import wait_random
from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a given number of random delays and returns them in sorted order.
    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay value in seconds.
    Returns:
        List[float]: A list of floats representing the random delays in sorted order.
    """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
