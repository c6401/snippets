def chunks(iterable, size):
    chunk = []
    for n, item in enumerate(iterable, 1):
        chunk.append(item)
        if n % size == 0:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
