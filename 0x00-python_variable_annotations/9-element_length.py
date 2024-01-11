#!/usr/bin/env python3
"""
annotates a given function’s parameters
and return values with the appropriate types
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """add type-annotation"""
    return [(i, len(i)) for i in lst]
