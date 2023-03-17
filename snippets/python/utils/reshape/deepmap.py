def deepmap(tree, fn):
    if isinstance(tree, dict):
        return {k: deepmap(v, fn) for k, v in tree.items()}
    if isinstance(tree, (list, tuple)):
        return [deepmap(v, fn) for v in tree]
    return fn(tree)
