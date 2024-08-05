#!/usr/bin/env python3
"""asynchronous function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Async function that waits for a random delay up to max_delay """
    waiting = random.uniform(0, max_delay)
    await asyncio.sleep(waiting)
    return (waiting)
