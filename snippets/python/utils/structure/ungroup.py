def ungroup(groupped):
    if isinstance(groupped, dict):
        for item, group in groupped.items():
            for record in ungroup(group):
                yield (item, *record)
    else:
        yield (groupped,)
