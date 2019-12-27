def groupby(seq, key):
    groups = {}
    for item in seq:
        groups.setdefault(key(item), []).append(item)
    return groups
