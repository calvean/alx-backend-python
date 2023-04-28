#!/usr/bin/env python3
""" Make Multiplier Module """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that returns a function
    Args:
        multiplier (float) - number to multiply with
    Return:
        function(float, float)
    """
    def mul_func(x: float) -> float:
        """
        Function that multiplies multiplier by x
        Args:
            x (float) - multiplicant
        Return:
            mul_func
        """
        return x * multiplier

    return mul_func
