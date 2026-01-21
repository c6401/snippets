def walk_list(ls):
    return [walk_tree(item) for item in ls]


def walk_dict(tree):
    return {k: walk_tree(v) for k, v in tree.items()}


def walk_tree(tree):
    match tree:
        case dict():
            return walk_dict(tree)
        case list():
            return walk_list(tree)
        case _:
            return tree
