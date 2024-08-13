#!/usr/bin/env python3
"""Type-annotated function that takes a list of
floats and return their sum"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of input_list"""
    return sum(input_list)
