"""
>>> build_tree([(1, 'a'), (3, 'b'), (2, 'c')])
[{'data': 'a', 'children': [{'data': 'b', 'children': [], 'level': 3}, \
{'data': 'c', 'children': [], 'level': 2}], 'level': 1}]
"""

def build_tree(pairs, factory=dict):
    """Builds nested tree from sequence of pairs: [(nest-level, data), ...]."""
    root = siblings = children = []
    previous_level = -1  # root level
    parents = []  # stack of parents

    for level, data in pairs:
        if level > previous_level:
            siblings = children  # prev node's children are current's siblings
            parents.append((previous_level, children))
        elif level < previous_level:
            while level <= parents[-1][0]:  # child's level should be > parent's
                parents.pop()
            siblings = parents[-1][1]  # set siblings as parent's children
        children = []
        siblings.append(factory(level=level, children=children, data=data))
        previous_level = level
    return root
