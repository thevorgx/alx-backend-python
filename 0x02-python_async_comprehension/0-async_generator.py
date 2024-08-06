#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """yield a number each iteration"""
    for _ in range(10):
        await asyncio.sleep(1)
        rand_number = uniform(0, 10)
        yield (rand_number)
