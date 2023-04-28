#!/usr/bin/env python3
""" Safely Get Value Module """

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Function that returns the value of the key
    Args:
        dct - dictitionary
        key (Any) - key of type Any
        default (T | None) - default
    Return:
        value (Any | T) - value of type Any or T
    """
    if key in dct:
        return dct[key]
    else:
        return default
