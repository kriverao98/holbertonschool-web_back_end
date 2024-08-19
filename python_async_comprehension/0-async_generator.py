#!/usr/bin/env python3
"""Coroutine called async_generator that takes no arguments."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields random delays between 0 and 10.
    """
    for i in range(10):
        delay = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield delay
