#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn n tasks that wait for a random delay
        between 0 and max_delay seconds."""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
