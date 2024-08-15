#!/usr/bin/env python3
"""Testing async functions"""
import random
import asyncio


async def wait_random(max_delay: float = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
