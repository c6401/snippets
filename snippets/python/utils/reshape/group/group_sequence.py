def group_seq(sequences):
    group = {}
    for n, *rest in sequences:
        group.setdefault(n, []).append(rest)
    return group
