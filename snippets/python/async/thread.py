import asyncio
from concurrent.futures import ThreadPoolExecutor

async def asyncronously(func, *args, **kwargs):
    def wrapper():
        return func(*args, **kwargs)
    
    with ThreadPoolExecutor(max_workers=1) as executor:
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(executor, wrapper)
        return await future
