#!/usr/bin/env python3
"""Annotating function to return appropriate types"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples where each tuple
    contains an element from lst and its length"""
    return [(i, len(i)) for i in lst]
