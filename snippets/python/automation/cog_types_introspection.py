[[[cog
import json
import subprocess as s
from datetime import datetime
from typing import *
result = {}
exec("""
class Data:
    field: int
""", globals(), result)
input = json.dumps({"data": {k: ((v.__args__[0].__name__, 1) if v.__name__ == 'Optional' else (v.__name__, 0)) for k, v in result['Data'].__annotations__.items()}})
print(s.run('jinja2 ____', input=input, capture_output=True, shell=True, text=True).stdout.strip())
]]]
[[[end]]]
'''
cog -rP ____
'''
