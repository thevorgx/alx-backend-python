#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from time import sleep
from random import uniform


async def async_generator():
    """yield a number each iteration"""
    for _ in range(10):
        sleep(1)
        rand_number = uniform(0, 10)
        yield (rand_number)
