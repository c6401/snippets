import json
from types import SimpleNamespace as Map

json.loads(___, object_hook=lambda o: Map(**o))
