def recursive_group(records):
    root = {}
    for record in records:
        node = root
        for value in record:
            node = node.setdefault(value, {})

    return root
