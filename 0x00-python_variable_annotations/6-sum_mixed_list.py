#!/usr/bin/env python3
""" Module to handle Mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Fuction to add int and float list
    Args:
        mxd_lst (list[int | float]) - list with ints or floats
    Return:
        (float) - sum of list items
    """
    sum: float = 0
    for item in mxd_lst:
        sum += item

    return sum
