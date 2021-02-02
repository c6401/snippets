async def achunks(iterable, size):
    chunk = []
    n = 1
    async for item in iterable:
        chunk.append(item)
        if n % size == 0:
            yield chunk
            chunk = []
        n += 1
    if chunk:
        yield chunk
