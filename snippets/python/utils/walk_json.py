def walk_json(
    json,
    dict_hook=lambda x: x,
    list_hook=lambda x: x,
    item_hook=lambda x: x,
    kv_hook=lambda k, v: (k, v)
):
    if isinstance(json, list):
        return list_hook([
            item_hook(walk_json(
                el,
                dict_hook=dict_hook,
                list_hook=list_hook,
                item_hook=item_hook,
                kv_hook=kv_hook,
            )) for el in json
        ])
    elif isinstance(json, dict):
        return dict_hook(dict(
            kv_hook(k, walk_json(
                v,
                dict_hook=dict_hook,
                list_hook=list_hook,
                item_hook=item_hook,
                kv_hook=kv_hook,
            )) for k, v in json.items()
        ))
    return json
