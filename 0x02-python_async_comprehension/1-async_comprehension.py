#!/usr/bin/env python3
"""Async comprehension
"""
from 0-async_generator import async_generator


async def async_comprehension():
    """
    Async comprehension
    """
    return [num async for num in async_generator()]
