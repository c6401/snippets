class YamlDict(FileDict):
    def __getitem__(self, key):
        with open(self.directory + '/' + key, 'r') as f:
            return yaml.safe_load(f)

    def __setitem__(self, key, value):
        with open(self.directory + '/' + key, 'w') as f:
            yaml.dump(value, f, version=(1, 2), default_flow_style=False, allow_unicode=True)
