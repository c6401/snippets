def groupby(iterable, keyfunc):
    groups = {}
    for item in iterable:
        groups.setdefault(keyfunc(item), []).append(item)
    return groups
