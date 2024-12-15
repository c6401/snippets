# pip install genson

from genson import SchemaBuilder

builder = SchemaBuilder()
builder.add_schema({"type": "object", "properties": {}})
builder.add_object({"str": "text"})
builder.add_object({"num": 5})

builder.to_schema()

print(builder.to_json(indent=2))
