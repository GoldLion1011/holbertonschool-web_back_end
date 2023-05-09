#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum of list of floats
    Args:
        mxd_lst (List[Union[int, float]]): list of floats
    Returns:
        float: sum of list of floats
    """
    return sum(mxd_lst)
