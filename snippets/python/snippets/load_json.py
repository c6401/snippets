import json
from types import SimpleNamespace

json.loads(..., object_hook=lambda o: SimpleNamespace(**o))
