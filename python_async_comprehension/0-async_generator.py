#!/usr/bin/env python3
""" Async Generator """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ define an asynchronous generator that awaits """
    for _ in range(10):
        await asyncio.sleep(1)  # define an asynchronous generator that awaits
        yield random.uniform(0, 10)  # yield a value to the caller
