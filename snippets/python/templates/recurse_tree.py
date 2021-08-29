def recurse_tree(tree):
    if isinstance(tree, dict):
        result = {}
        for key, value in tree.items():
            result[key] = recurse_tree(value)
        return result

    elif isinstance(tree, list):
        result = []
        for item in tree:
            result.append(recurse_tree(item))
        return result

    elif isinstance(tree, str):
        return tree

    elif isinstance(tree, int):
        return tree

    elif isinstance(tree, bool):
        return tree

    elif tree is None:
        return tree

    return tree
