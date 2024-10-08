#!/usr/bin/env python3
"""Async generator"""
import asyncio
import random


async def async_generator():
    """
    Async generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
