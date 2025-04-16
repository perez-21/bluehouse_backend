wait_random = __import__("0-basic_async_syntax").wait_random
import asyncio


async def wait_n(n, max_delay):
    delays = await asyncio.gather(*(wait_random(max_delay) for i in range(0, n)))
    return delays
