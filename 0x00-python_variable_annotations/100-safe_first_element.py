#!/usr/bin/env python3
""" Safe first Element Module """
from typing import Optional, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Function to return first element
    Args:
        list (list) - list of elements
    Return:
        first element, else None
    """
    if lst:
        return lst[0]
    else:
        return None
