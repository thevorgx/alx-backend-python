#!/usr/bin/env python3
"""asynchronous function"""
from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Async function that waits for a random delay up to max_delay """
    waiting = uniform(0, max_delay)
    await sleep(waiting)
    return (waiting)
