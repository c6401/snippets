def flatten_tree(tree):
    if isinstance(tree, dict):
        for item, group in tree.items():
            for record in flatten_tree(group):
                yield (item, *record)
    else:
        yield (tree,)
