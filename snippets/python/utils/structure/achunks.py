async def achunks(seq, size):
    chunk = []
    n = 1
    async for item in seq:
        chunk.append(item)
        if n % size == 0:
            yield chunk
            chunk = []
        n += 1
    if chunk:
        yield chunk
