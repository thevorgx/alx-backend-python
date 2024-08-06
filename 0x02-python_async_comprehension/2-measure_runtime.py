#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """run 4 tasks in parallel and return total run_time"""
    t0 = time()

    task1 = asyncio.create_task(async_comprehension())
    task2 = asyncio.create_task(async_comprehension())
    task3 = asyncio.create_task(async_comprehension())
    task4 = asyncio.create_task(async_comprehension())

    await asyncio.gather(task1, task2, task3, task4)

    tf = time()

    run_time = tf - t0

    return (run_time)
