def window(iterable, size=2):
    seq = iter(iterable)

    frame = tuple(next(iterable) for i in range(size))
    yield frame

    for item in iterable:
        frame = frame[1:] + (item,)
        yield frame
