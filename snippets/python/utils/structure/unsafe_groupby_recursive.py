def window(collection, size=2):
    for i in range(len(collection) - size + 1):
        yield collection[i: i + size]


def recursive_group(seq):
    root = {}
    for record in seq:
        node = root
        node_parent = None
        for grand, parent, item in window([None, *record], 3):
            if isinstance(node, dict):
                node_parent, node = node, node.setdefault(parent, item)
            else:
                node_parent[grand] = node_parent = {parent: item}
                node = item

    return root
