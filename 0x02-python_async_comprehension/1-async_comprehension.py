#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine that collect random numbers for async_gen"""
    listo = []
    async for i in async_generator():
        listo.append(i)
    return (listo)
