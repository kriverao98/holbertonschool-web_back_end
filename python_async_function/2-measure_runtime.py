#!/usr/bin/env python3
"""Task test async functions"""
import time
import asyncio
from concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of the wait_n function by running it 'n' times with a maximum delay of 'max_delay'.
    Args:
        n (int): The number of times to run the wait_n function.
        max_delay (int): The maximum delay for each call to the wait_n function.
    Returns:
        float: The average runtime of the wait_n function.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
