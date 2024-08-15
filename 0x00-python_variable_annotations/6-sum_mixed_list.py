#!/usr/bin/env python3
""" Mixed list Module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum Mixed list
    """
    return float(sum(mxd_lst))
