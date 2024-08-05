#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """exec wait_random n times"""
    listo = []
    for value in range(n):
        value = await wait_random(max_delay)
        listo.append(value)
    new_listo = sorted(listo)
    return (new_listo)
