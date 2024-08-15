#!/usr/bin/env python3
import asyncio
from basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task that waits for a random amount of time.
    :param max_delay: The maximum delay in seconds.
    :return: An asyncio Task object.
    """

    return asyncio.create_task(wait_random(max_delay))
