#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yield a number each iteration"""
    for _ in range(10):
        await asyncio.sleep(1)
        rand_number = random.uniform(0, 10)
        yield (rand_number)
