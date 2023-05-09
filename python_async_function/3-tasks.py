#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a task that waits for a random delay
        between 0 and max_delay seconds."""
    return asyncio.create_task(wait_random(max_delay))
