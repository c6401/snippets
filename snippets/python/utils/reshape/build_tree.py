"""
>>> build_tree([(1, 'a'), (2, 'b'), (3, 'c'), (2, 'd')])
[{'level': 1, 'children': [{'level': 2, 'children': [{'level': 3, \
'children': [], 'data': 'c'}], 'data': 'b'}, {'level': 2, 'children': [], \
'data': 'd'}], 'data': 'a'}]
"""

def build_tree(pairs, factory=dict):
    """Builds nested tree from sequence of pairs: [(nest-level, data), ...]."""
    root = children = []
    previous_level = -1  # root level
    stack = []  # stack of parent nodes

    for level, data in pairs:
        if level > previous_level:
            stack.append((previous_level, children))
        while level <= stack[-1][0]:  # child's level should be > parent's
            stack.pop()
        children = []
        stack[-1][1].append(factory(level=level, children=children, data=data))
        previous_level = level
    return root
