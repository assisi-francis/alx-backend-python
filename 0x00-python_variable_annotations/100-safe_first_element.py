#!/usr/bin/env python3
"""
Annotate with optional
"""


from typing import Any, Optional


def safe_first_element(lst: list) -> Optional[Any]:
    """ takes a list """
    if lst:
        return lst[0]
    else:
        return None
