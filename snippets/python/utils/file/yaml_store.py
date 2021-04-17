from contextlib import contextmanager
from ruamel import yaml


yml = yaml.YAML()


@contextmanager
def store(path):
    try:
        with open(path) as f:
            data = yml.load(f)
    except FileNotFoundError:
        data = {}

    yield data

    with open(path, 'w') as f:
        yml.dump(data, f)
