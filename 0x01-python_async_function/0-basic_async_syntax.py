#!/usr/bin/env python3
"""Async function"""

from random import uniform
from asyncio import sleep


async def wait_random(max_delay=10):
    """Async function that takes max delay of 10"""
    waiting = uniform(0, max_delay)
    await sleep(waiting)
    return (waiting)
