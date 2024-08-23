#!/usr/bin/env python3
"""Concurrent module"""
from 0-basic_async_syntax import wait_random
import asyncio
from typing import List


async def wait_n(n: int, delay: int = 10) -> List[float]:
    """
    Wait of delay function
    """
    list_of_delays = []
    async def wait_and_append():
        delay = await wait_random(delay)
        list_of_delays.append(delay)
        return delay

    await asyncio.gather(*(wait_and_append() for _ in range(n)))
    return sorted(list_of_delays)
