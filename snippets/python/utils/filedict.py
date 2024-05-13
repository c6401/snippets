import os

class FileDict:
    def __init__(self, directory):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def __getitem__(self, key):
        with open(self.directory + '/' + key, 'r') as f:
            return f.read()

    def __setitem__(self, key, value):
        with open(self.directory + '/' + key, 'w') as f:
            f.write(value)

    def __delitem__(self, key):
        os.remove(self.directory + '/' + key)

    def __iter__(self):
        return iter(os.listdir(self.directory))

    def __len__(self):
        return len(os.listdir(self.directory))

    def __contains__(self, key):
        return os.path.exists(self.directory + '/' + key)

    def __str__(self):
        return str({key: self[key] for key in self})

    def __repr__(self):
        return str(self)

