def walk_tree(tree, key='children'):
    for item in tree:
        yield item
        if key in tree:
            yield from walk_tree(tree[key], key)
