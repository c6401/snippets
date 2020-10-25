import asyncio
from concurrent.futures import ThreadPoolExecutor

def run_in_thread(func, _workers=1, *args, **kwargs):
    with ThreadPoolExecutor(max_workers=_workers) as executor:
        loop = asyncio.get_event_loop()
        return loop.run_in_executor(executor, lambda: func(*args, **kwargs))
