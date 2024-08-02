#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """tuple with a string and the square of a number"""
    square_v: float = v ** 2
    tup: Tuple[str, float] = (k, square_v)
    return (tup)
