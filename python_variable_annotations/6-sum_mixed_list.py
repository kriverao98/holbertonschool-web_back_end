#!/usr/bin/env python3
"""Typed-annotated function that returns their sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of ints and floats"""
    return sum(mxd_lst)
