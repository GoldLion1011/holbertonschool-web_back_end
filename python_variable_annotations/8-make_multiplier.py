#!/usr/bin/env python3
"""Complex types - list of floats"""
from typing import List, Union


def make_multiplier(multiplier: float) -> callable:
    """Returns a function that multiplies a float by multiplier
    Args:
        multiplier (float): multiplier
    Returns:
        callable: function that multiplies a float by multiplier
    """
    def multiply_by_multiplier(x: float) -> float:
        """Multiplies a float by multiplier
        Args:
            x (float): number to multiply
        Returns:
            float: x multiplied by multiplier
        """
        return x * multiplier
    return multiply_by_multiplier
