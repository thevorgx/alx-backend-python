#!/usr/bin/env python3
"""return a function that multiply a float val by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that multiply a float val by multiplier"""
    def vorg_multiplier_dynamo(v: float) -> float:
        """function to return result"""
        res = v * multiplier
        return (res)
    return(vorg_multiplier_dynamo)
