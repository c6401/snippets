def window(seq, size=2):
    seq = iter(seq)

    frame = tuple(next(seq) for i in range(size))
    yield frame

    for item in seq:
        frame = frame[1:] + (item,)
        yield frame
