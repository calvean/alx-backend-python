#!/usr/bin/env python3
""" Module for complex Types """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Fuction that takes k and v and return a tupple
    Args:
        k (str) - first argument
        v (int | float) - second argument
    Return:
        [k, v^2] (str, float)
    """
    sqr: float = v**2

    return [k, sqr]
