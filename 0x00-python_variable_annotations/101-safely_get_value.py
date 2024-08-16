#!/usr/bin/env python3
""" Mapping Module"""
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[TypeVar, None] = None) -> Union[Any, TypeVar]:
    """ More Mappings
    """
    if key in dct:
        return dct[key]
    else:
        return default
