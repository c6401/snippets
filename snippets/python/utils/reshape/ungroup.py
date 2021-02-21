def ungroup_records(tree):
    if isinstance(tree, dict):
        for item, group in tree.items():
            for record in ungroup(group):
                yield (item, *record)
    else:
        yield (tree,)
