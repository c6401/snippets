#!/usr/bin/env python3
'''
JSON sample(s) -> JTD (RFC 8927). Root type is named by the first argument.

    ./jtd_infer.py User sample.json [more.json ...] > user.jtd.json
'''
import json, re, sys
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
        case [*items]: return {'elements': merge_all([infer(i) for i in items])}
        case dict(): return {'properties': {k: infer(x) for k, x in v.items()}}
    return {}


def merge(a, b):
    return merge_all([a, b])


def merge_all(schemas):
    """Merge every schema in one pass. Pairwise folding is quadratic; this is linear."""
    null = any(s.get('nullable') for s in schemas)
    bare = [{k: v for k, v in s.items() if k != 'nullable'} for s in schemas]
    return _merge_all([s for s in bare if s]) | ({'nullable': True} if null else {})


def _merge_all(ss):
    if not ss:
        return {}
    if len(ss) == 1:
        return ss[0]
    if all(_obj(s) for s in ss):
        return _props_all(ss)
    if all('elements' in s for s in ss):
        return {'elements': merge_all([s['elements'] for s in ss])}
    if all('ref' in s for s in ss):
        return ss[0] if len({s['ref'] for s in ss}) == 1 else {}
    if all('type' in s for s in ss):
        return _types_all([s['type'] for s in ss])
    return {}


def _types_all(types):
    out = types[0]
    for t in types[1:]:
        if t == out:
            continue
        if frozenset((out, t)) not in WIDE:
            return {}
        out = WIDE[frozenset((out, t))]
    return {'type': out}


def _props_all(ss):
    groups, seen = {}, {}
    for s in ss:
        for grp in ('properties', 'optionalProperties'):
            for k, v in s.get(grp, {}).items():
                groups.setdefault(k, []).append(v)
                if grp == 'properties':
                    seen[k] = seen.get(k, 0) + 1
    req = {k: merge_all(vs) for k, vs in groups.items() if seen.get(k) == len(ss)}
    opt = {k: merge_all(vs) for k, vs in groups.items() if seen.get(k) != len(ss)}
    return {'properties': req} | ({'optionalProperties': opt} if opt else {})


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
    schemas = []
    for i, sample in enumerate(samples):
        schemas.append(infer(sample))
    defs = {}
    return hoist(merge_all(schemas), defs, (name,)) | {'definitions': defs}


if __name__ == '__main__':
    name, files = sys.argv[1], sys.argv[2:]
    blobs = [json.loads(Path(f).read_text()) for f in files] or [json.load(sys.stdin)]
    json.dump(jtd(name, blobs), sys.stdout, indent=2)
