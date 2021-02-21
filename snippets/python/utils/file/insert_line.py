def insert_line(file, text, after=None, before=None, past=None, once=True):
    with open(file) as f:
        lines = iter(f.readlines())

    with open(file, 'w') as f:
        if past:
            for line in lines:
                f.write(line)
                if re.match(past, line):
                    break

        for line in lines:
            if before and re.match(before, line):
                 f.write(text + '\n')
                 if once:
                     f.write(line)
                     break

            f.write(line)

            if after and re.match(after, line):
                 f.write(text + '\n')
                 if once:
                     break

        for line in lines:
            f.write(line)
