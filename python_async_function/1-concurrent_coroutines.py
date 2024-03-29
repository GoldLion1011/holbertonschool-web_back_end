#!/usr/bin/env python3
"""Concurrent coroutines"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn wait_random n times with the specified max_delay."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)
    return sorted(delays)
