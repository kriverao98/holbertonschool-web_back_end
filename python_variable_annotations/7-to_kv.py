#!/usr/bin/env python3
"""Type-annotated function that takes a type as arg and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, float(v * v))
