def deepmap(tree, fn): return {k: deepmap(v, fn) for k, v in tree.items()} if isinstance(tree, dict | tuple) else [deepmap(v, fn) for v in tree] if isinstance(tree, list) else fn(tree)
