#!/usr/bin/env python3
"""Use mypy"""
from typing import Tuple, List, Sequence


def zoom_array(lst: Sequence[int], factor: int = 2) -> List[int]:
    """ Zoomed array
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
