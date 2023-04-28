#!/usr/bin/env python3
""" Module to add lists """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function that add floats in a list
    Args:
        input_list (list[float]) - list of floats
    Return:
        (float) - sum of floats
    """
    sum: float = 0

    for item in input_list:
        sum += item

    return sum
