def chunks(seq, size):
    chunk = []
    for n, item in enumerate(seq, 1):
        chunk.append(item)
        if n % size == 0:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
