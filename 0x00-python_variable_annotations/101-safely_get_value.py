#!/usr/bin/env python3
"""
add type annotations to the function
given the parameters and the return values
"""
from typing import TypeVar, Mapping, Any, Union, Optional
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Optional[T] = None
) -> Union[Any, T]:
    """add type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
