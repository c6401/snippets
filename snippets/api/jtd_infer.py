#!/usr/bin/env python3
'''
JSON sample(s) -> JTD (RFC 8927). Root type is named by the first argument.

    ./jtd_infer.py User sample.json [more.json ...] > user.jtd.json
'''
import json, re, sys
from functools import reduce
from pathlib import Path

TS = re.compile(r'\d{4}-\d\d-\d\dT[\d:.]+(Z|[+-][\d:]+)$')
WIDE = {frozenset(('int32', 'float64')): 'float64', frozenset(('timestamp', 'string')): 'string'}


def infer(v):
    match v:
        case None: return {'nullable': True}
        case bool(): return {'type': 'boolean'}
        case int(): return {'type': 'int32'}
        case float(): return {'type': 'float64'}
        case str(): return {'type': 'timestamp' if TS.match(v) else 'string'}
        case []: return {'elements': {}}
        case [*items]: return {'elements': reduce(merge, map(infer, items))}
        case dict(): return {'properties': {k: infer(x) for k, x in v.items()}}
    return {}


def merge(a, b):
    n = {'nullable': True} if a.get('nullable') or b.get('nullable') else {}
    a = {k: v for k, v in a.items() if k != 'nullable'}
    b = {k: v for k, v in b.items() if k != 'nullable'}
    if not a or not b or a == b:
        return (a or b) | n
    match a, b:
        case {'type': x}, {'type': y}:
            return ({'type': WIDE[frozenset((x, y))]} if frozenset((x, y)) in WIDE else {}) | n
        case {'elements': x}, {'elements': y}:
            return {'elements': merge(x, y)} | n
    if _obj(a) and _obj(b):
        return _props(a, b) | n
    return n


def hoist(s, defs, path):
    n = {'nullable': True} if s.get('nullable') else {}
    if 'elements' in s:
        return {'elements': hoist(s['elements'], defs, path[:-1] + (_singular(path[-1]),))} | n
    if _obj(s):
        body = {g: {k: hoist(v, defs, path + (k,)) for k, v in s[g].items()}
                for g in ('properties', 'optionalProperties') if g in s}
        return {'ref': _uniq([_pascal(path[-1]), _join(path[-2:]), _join(path)], body, defs)} | n
    return s


def _obj(s):
    return 'properties' in s or 'optionalProperties' in s


def _props(a, b):
    ap, bp = a.get('properties', {}), b.get('properties', {})
    av, bv = ap | a.get('optionalProperties', {}), bp | b.get('optionalProperties', {})
    keys = dict.fromkeys([*av, *bv])
    req = {k: merge(av[k], bv[k]) for k in keys if k in ap and k in bp}
    opt = {k: merge(av[k], bv[k]) if k in av and k in bv else av.get(k) or bv.get(k)
           for k in keys if k not in req}
    return {'properties': req} | ({'optionalProperties': opt} if opt else {})


def _pascal(s):
    return ''.join(w[:1].upper() + w[1:] for w in re.split(r'[^0-9a-zA-Z]+', s) if w)


def _join(path):
    return ''.join(_pascal(p) for p in path)


def _singular(s):
    return s[:-1] if len(s) > 2 and s.endswith('s') and not s.endswith('ss') else s


def _uniq(names, body, defs):
    for k, v in defs.items():
        if v == body:
            return k
    for n in dict.fromkeys(names):
        if n not in defs:
            defs[n] = body
            return n
    n, i = names[-1], 2
    while f'{n}{i}' in defs:
        i += 1
    defs[f'{n}{i}'] = body
    return f'{n}{i}'


def jtd(name, samples):
    defs = {}
    root = hoist(reduce(merge, map(infer, samples)), defs, (name,))
    return root | {'definitions': defs}


if __name__ == '__main__':
    name, files = sys.argv[1], sys.argv[2:]
    blobs = [json.loads(Path(f).read_text()) for f in files] or [json.load(sys.stdin)]
    json.dump(jtd(name, blobs), sys.stdout, indent=2)
