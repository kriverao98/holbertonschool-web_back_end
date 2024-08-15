#!/usr/bin/env python3
"""Testing async functions"""
from basic_async_syntax import wait_random
from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
