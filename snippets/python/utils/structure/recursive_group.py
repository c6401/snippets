def recursive_group(seq):
    root = {}
    for items in seq:
        node = root
        for item in items:
            parent = node
            node = node.setdefault(item, {})
            if not node:
                parent[item] = node = {}
        parent[item] = None

    return root
