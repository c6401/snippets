def window(seq, size=2):
    for i in range(len(seq) - size + 1):
        yield seq[i: i + size]
