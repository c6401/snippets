def r(o, d=lambda x: x, l=lambda x: x, v=lambda x: x): return d({k: r(v) for k, v in o.items()}) if isinstance(o, dict) else l([r(i) for i in o]) if isinstance(o, list) else v(o)
