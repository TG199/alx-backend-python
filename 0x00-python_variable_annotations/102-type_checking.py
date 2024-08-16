#!/usr/bin/env python3
"""Use mypy"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """ Zoomed array
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 9)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
