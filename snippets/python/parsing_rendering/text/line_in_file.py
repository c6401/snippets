with open(___, 'r+') as f:
    if value + '\n' not in f.readlines():
        f.write(value + '\n')
