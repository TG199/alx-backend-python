#!/usr/bin/env python3
"""Measure module"""
import time
import asyncio
from 1-async_comprehension import async_comprehension


async def measure_runtime():
    """
    Measure runtime
    """
    start_time = time.time()

    results = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
