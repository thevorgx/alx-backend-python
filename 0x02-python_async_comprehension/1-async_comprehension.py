#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine that collect random numbers for async_gen"""
    return [rand_number async for rand_number in async_generator()]
