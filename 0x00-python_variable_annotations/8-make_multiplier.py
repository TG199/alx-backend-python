#!/usr/bin/env python3
"""Returning function Module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function

    """
    def multi(m: float) -> float:
        return m * multiplier
    return multi
