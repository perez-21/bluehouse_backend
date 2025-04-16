task_wait_random = __import__("3-tasks").task_wait_random

import asyncio


async def task_wait_n(n, max_delay):
    delays = []
    for i in range(0, n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)

    return delays
