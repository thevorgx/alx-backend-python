#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """run 4 tasks in parallel and return total run_time"""
    tasks = []
    t0 = time()

    for _ in range(4):
        task = asyncio.create_task(async_comprehension())
        tasks.append(task)

    await asyncio.gather(*tasks)

    tf = time()

    run_time = tf - t0

    return (run_time)
