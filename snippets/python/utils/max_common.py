def max_common(a, b):
    for n, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return n
    return n + 1
