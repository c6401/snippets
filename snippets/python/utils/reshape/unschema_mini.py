def getref(ref):
    result = api
    for segment in ref.split('/')[1:]:
        result = result[segment]
    return result


def _unprimitive(s):
    match s:
        case {"examples": list(e)}: return e[0]
        case {"enum": list(e)}: return e[0]
    return


def unschema(s):
    match s:
        case {"$ref": ref}: return unschema(getref(ref))
        case {"anyOf": ls}: return next((unschema(i) for i in ls if i), None)
        case {"type": "null"}: return
        case {"type": "integer"}: return _unprimitive(s) or 1
        case {"type": "array"}: return unschema(s["items"])
        case {"type": "object"}: return {k: unschema(v) for k, v in s["properties"].items()}
        case {"type": "string"}: return _unprimitive(s) or "foobar"
    return s
