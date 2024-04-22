def group(pairs):
    groups = {}
    for key, item in pairs:
        groups.setdefault(key, []).append(item)
    return groups
