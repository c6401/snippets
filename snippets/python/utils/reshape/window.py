def window(iterable, size=2):
    iterable = iter(iterable)

    frame = tuple(next(iterable) for _ in range(size))
    yield frame

    for item in iterable:
        frame = frame[1:] + (item,)
        yield frame
