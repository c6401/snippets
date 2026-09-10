#!/usr/bin/env python3
'''
JSON -> JTD (RFC 8927).

    ./jtd_infer.py sample.json > sample.jtd.json
'''
import json, re, sys
from pathlib import Path

RFC3339 = re.compile(r'\d{4}-\d\d-\d\dT[\d:.]+(Z|[+-][\d:]+)$')
WIDER = {'int32': 'float64', 'timestamp': 'string'}


def infer(value):
    match value:
        case None: return {'nullable': True}
        case bool(): return {'type': 'boolean'}          # before int: bool subclasses int
        case int(): return {'type': 'int32'}
        case float(): return {'type': 'float64'}
        case str(): return {'type': 'timestamp' if RFC3339.match(value) else 'string'}
        case list(): return {'elements': merge(value)}
        case dict(): return {'properties': {k: infer(v) for k, v in value.items()}}


def merge(values):
    known = [v for v in values if v is not None]
    if not known:
        schema = {}
    elif len(known) == 1:
        schema = infer(known[0])
    elif all(isinstance(v, dict) for v in known):
        schema = merge_objects(known)
    elif all(isinstance(v, list) for v in known):
        schema = {'elements': merge([item for v in known for item in v])}
    elif any(isinstance(v, (dict, list)) for v in known):
        schema = {}                            # a container mixed in with scalars
    else:                                      # scalars: find the kind they all widen into
        kinds = {infer(v)['type'] for v in known}
        schema = next(({'type': k} for k in kinds
                       if all(x == k or WIDER.get(x) == k for x in kinds)), {})
    if len(known) < len(values):
        schema['nullable'] = True
    return schema


def merge_objects(values):
    fields = {}                                # key -> every value seen under it
    for v in values:
        for k, x in v.items():
            fields.setdefault(k, []).append(x)
    always = {k: merge(xs) for k, xs in fields.items() if len(xs) == len(values)}
    maybe = {k: merge(xs) for k, xs in fields.items() if len(xs) != len(values)}
    return {'properties': always} | ({'optionalProperties': maybe} if maybe else {})


if __name__ == '__main__':
    json.dump(infer(json.loads(Path(sys.argv[1]).read_text())), sys.stdout, indent=2)
