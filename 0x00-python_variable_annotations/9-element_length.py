#!/usr/bin/env python3
""" Element Length Module """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes a list and returns a list
    Args:
        lst (iterable) - an iterable list
    Return:
        tuple
    """
    return [(i, len(i)) for i in lst]
