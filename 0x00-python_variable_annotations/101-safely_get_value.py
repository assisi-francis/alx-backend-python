#!/usr/bin/env python3
"""
Given the parameters and the return values
add type annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""


from typing import Dict, TypeVar, Optional


T = TypeVar('T')


def safely_get_value(dct: Dict[str, T], key: str,
                     default: Optional[T] = None) -> Optional[T]:
    if key in dct:
        return dct[key]
    else:
        return default
