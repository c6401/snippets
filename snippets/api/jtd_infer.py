#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pyyaml"]
# ///
'''
JSON samples -> JTD (RFC 8927) + op metadata, for minijinja-cli templates.

    ./jtd_infer.py api.yaml > api.json
'''
import json, re, sys
from functools import reduce
from pathlib import Path

import yaml

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
            return ({'type': x} if x == y else {'type': WIDE[frozenset((x, y))]} if frozenset((x, y)) in WIDE else {}) | n
        case {'elements': x}, {'elements': y}:
            return {'elements': merge(x, y)} | n
    if _obj(a) and _obj(b):
        return _props(a, b) | n
    return n


def _obj(s):
    return 'properties' in s or 'optionalProperties' in s


def _props(a, b):
    ap, bp = a.get('properties', {}), b.get('properties', {})
    av = ap | a.get('optionalProperties', {})
    bv = bp | b.get('optionalProperties', {})
    keys = dict.fromkeys([*av, *bv])
    both = [k for k in keys if k in ap and k in bp]
    req = {k: merge(av[k], bv[k]) for k in both}
    opt = {k: merge(av[k], bv[k]) if k in av and k in bv else av.get(k) or bv.get(k)
           for k in keys if k not in req}
    return {'properties': req} | ({'optionalProperties': opt} if opt else {})


def hoist(s, defs, path=('root',), name=None):
    n = {'nullable': True} if s.get('nullable') else {}
    if 'elements' in s:
        return {'elements': hoist(s['elements'], defs, path[:-1] + (_singular(path[-1]),), name)} | n
    if _obj(s):
        body = {g: {k: hoist(v, defs, path + (k,)) for k, v in s[g].items()}
                for g in ('properties', 'optionalProperties') if g in s}
        if name:
            defs[name] = merge(defs[name], body) if name in defs else body
            return {'ref': name} | n
        return {'ref': _uniq([_pascal(path[-1]), _join(path[-2:]), _join(path)], body, defs)} | n
    return s


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


def op(spec, defs):
    samples = [json.loads(Path(s).read_text()) for s in _list(spec.get('sample'))]
    root = hoist(reduce(merge, map(infer, samples)), defs, (spec['name'],), spec.get('type')) if samples else {}
    return {
        'name': spec['name'],
        'method': spec.get('method', 'GET').upper(),
        'path': spec['path'],
        'url': re.sub(r'{(\w+)}', r'${\1}', spec['path']),
        'params': re.findall(r'{(\w+)}', spec['path']),
        'query': _list(spec.get('query')),
        'body': spec.get('body'),
        'returns': root,
    }


def _refs(s):
    match s:
        case {'ref': r}: return [r]
        case {'elements': e}: return _refs(e)
    return []


def _list(v):
    return [] if v is None else v if isinstance(v, list) else [v]


def main(path):
    spec = yaml.safe_load(Path(path).read_text())
    defs = {}
    ops = [op(o, defs) for o in spec['ops']]
    used = {r for o in ops for r in _refs(o['returns'])} | {o['body'] for o in ops if o['body']}
    return {'definitions': defs,
            'metadata': {'base': spec.get('base', ''), 'imports': sorted(used), 'ops': ops}}


if __name__ == '__main__':
    json.dump(main(sys.argv[1]), sys.stdout, indent=2)
