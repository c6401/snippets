def window(iterable, size=2):
    iterable = iter(iterable)
    frame = (None, *(next(iterable) for _ in range(size-1)))
    for item in iterable:
        frame = (*frame[1:], item)
        yield frame
