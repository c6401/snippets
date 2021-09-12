def index_sections(lines, symbol='#', sep=' '):
    index = []
    level_re = re.compile(fr'(?:(\{symbol}+)\{sep})?')
    for n, line in enumerate(lines):
        level = len(level_re.match(line).groups()[0] or '')
        if level:
            index.append({'l': n, 'lvl': level})
    return index
