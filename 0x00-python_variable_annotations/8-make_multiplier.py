#!/usr/bin/env python3
"""
a type-annotated function make_multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function multiples"""
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
