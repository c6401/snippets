def window(collection, size=2):
    for i in range(len(collection) - size + 1):
        yield collection[i: i + size]
