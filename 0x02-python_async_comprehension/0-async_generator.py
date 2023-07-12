#!/usr/bin/env python3
"""
async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    '''loop 10 times, each time async wait 1 sec, yield random num 0-9'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
