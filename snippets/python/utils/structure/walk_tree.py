def walk_tree(items, key):
    for item in items:
        yield item
        if key in item:
            yield from walk_tree(item[key], key)
