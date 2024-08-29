Json = dict[str, 'Json'] | list['Json'] | str | int | float | bool | None


class Unschema(object):
    def __init__(self, spec: Json = None):
        self.spec = spec

    def __call__(self, schema: Json) -> Json:
        return self.schema(schema)

    def ref(self, schema: dict[str, Json]) -> Json:
        assert '$ref' in schema and isinstance(schema['$ref'], str)
        path = schema['$ref'].split('/')[1:]
        spec = self.spec
        for p in path:
            assert isinstance(spec, dict)
            spec = spec[p]
        return self.schema(spec)

    def enum(self, schema: dict[str, Json]) -> Json:
        assert 'enum' in schema and isinstance(schema['enum'], list)
        return schema['enum'][0]

    def string(self, schema: dict[str, Json]) -> Json:
        if 'enum' in schema:
            return self.enum(schema)
        if 'const' in schema:
            return schema['const']
        return schema

    def array(self, schema: dict[str, Json]) -> Json:
        items = schema.get('items')
        if items:
            return [self.schema(items)]
        return schema

    def object(self, schema: dict[str, Json]) -> Json:
        properties = schema.get('properties')
        if properties:
            assert isinstance(properties, dict)
            return {k: self.schema(v) for k, v in properties.items()}
        return schema

    def type(self, schema: dict[str, Json]) -> Json:
        if schema['type'] == 'object':
            return self.object(schema)
        if schema['type'] == 'array':
            return self.array(schema)
        if schema['type'] == 'string':
            return self.string(schema)
        return schema

    def one_of(self, schema: dict[str, Json]) -> Json:
        assert 'oneOf' in schema and isinstance(schema['oneOf'], list)
        return self.schema(schema['oneOf'][0])

    def all_of(self, schema: dict[str, Json]) -> Json:
        assert 'allOf' in schema and isinstance(schema['allOf'], list)
        return self.schema(schema['allOf'][0])

    def any_of(self, schema: dict[str, Json]) -> Json:
        assert 'anyOf' in schema and isinstance(schema['anyOf'], list)
        return self.schema(schema['anyOf'][0])

    def dict(self, schema: dict[str, Json]) -> Json:
        if '$ref' in schema:
            return self.ref(schema)
        if 'example' in schema:
            return schema['example']
        if 'type' in schema:
            self.type(schema)
        if 'anyOf' in schema:
            return self.any_of(schema)
        if 'allOf' in schema:
            return self.all_of(schema)
        if 'oneOf' in schema:
            return self.one_of(schema)
        return schema

    def schema(self, schema: Json) -> Json:
        if isinstance(schema, dict):
            return self.dict(schema)
        return schema
