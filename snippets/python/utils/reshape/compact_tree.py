def compact_tree(tree, sep='.'):
    # [{"a": {"b": 1}}] -> [{"a.b": 1}]
    if isinstance(tree, dict):
        items = list(tree.items())
        if len(items) == 1:
            key, value = items[0]
            nested = compact_tree(value)
            if isinstance(nested, dict):
                return {f'{key}{sep}{k}': v for k, v in nested.items()}
        return {k: compact_tree(v) for k, v in items}

    elif isinstance(tree, list):
        return [compact_tree(i) for i in tree]

    return tree
