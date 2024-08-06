#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """yield a number each iteration"""
    for _ in range(10):
        await asyncio.sleep(1)
        rand_number = random.uniform(0, 10)
        if rand_number == 0:
            rand_number += 0.01
        elif rand_number == 10:
            rand_number -= 0.01
        yield (rand_number)
