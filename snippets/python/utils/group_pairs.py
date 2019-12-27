def group(seq):
    groups = {}
    for key, item in seq:
        groups.setdefault(key, []).append(item)
    return groups
