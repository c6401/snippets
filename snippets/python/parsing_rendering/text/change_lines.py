new = []

with open(file) as f:
    lines = iter(f.readlines())

for line in lines:
    new.append(line)

with open(file, 'w') as f:
    f.write('\n'.join(new))
