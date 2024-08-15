#!/usr/bin/env python3
"""Annotate function Module
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return the length of element
    """
    return [(i, len(i)) for i in lst]
