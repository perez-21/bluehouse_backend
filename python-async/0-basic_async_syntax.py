import random
import asyncio


async def wait_random(max_delay=10):
    actual_delay = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
