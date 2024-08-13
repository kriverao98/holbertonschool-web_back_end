#!/usr/bin/env python3
"""Type-annotated function that takes a float multiplier and returns a function that multiplies a float by this multiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies its input by the given multiplier"""
    def multiplier_function(value: float) -> float:
        return multiplier * value
    
    return multiplier_function
