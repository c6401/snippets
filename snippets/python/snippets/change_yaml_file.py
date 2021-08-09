from ruamel import yaml

path = '???'

yml = yaml.YAML()

with open(path) as f:
    data = yml.load(f)

with open(path, 'w') as f:
    yml.dump(data, f)
