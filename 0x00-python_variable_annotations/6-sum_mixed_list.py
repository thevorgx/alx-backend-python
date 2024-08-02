#!/usr/bin/env python3
"""sum mixed list of floats and ints"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """mixed list sum dynamo"""
    mxd_listo = sum(mxd_lst)
    return (mxd_listo)
