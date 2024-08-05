#!/usr/bin/env python3
"""Measure the runtime"""
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average execution time of wait_n"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    total_time = end - start
    return (total_time / n)
