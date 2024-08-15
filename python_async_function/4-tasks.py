#!/usr/bin/env python3
"""
Sorts a list of delays obtained from running multiple
instances of the `task_wait_random` coroutine.

Args:
    n (int): The number of instances of `task_wait_random`
    to run.
    max_delay (int): The maximum delay for each instance of
    `task_wait_random`.

Returns:
    List[int]: A sorted list of delays.
"""

import asyncio
from tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int):
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
