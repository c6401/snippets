def build_tree(pairs, factory=dict):
    """Builds nested tree from sequence of pairs: [(nest-level, data), ...]."""
    root = siblings = previous_node_children = []
    previous_level = -1  # root level
    parents = []

    for level, data in pairs:
        children = []
        node = factory(level=level, children=children, data=data)
        if level > previous_level:
            siblings = previous_node_children
            parents.append((previous_level, previous_node_children))
        elif level < previous_level:
            while level <= parents[-1][0]:  # parent's level
                parents.pop()
            siblings = parents[-1][1]  # parent's children
        siblings.append(node)
        previous_level = level
        previous_node_children = children
    return root
