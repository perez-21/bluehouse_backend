import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n, max_delay):
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_elapsed = time.perf_counter() - start_time
    return time_elapsed
