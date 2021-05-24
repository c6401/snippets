import re

def get_line_slice(lines, start, end):
    lines = iter(lines)
    for line in lines:
        if re.match(start, line):
            break
    for line in lines:
        if re.match(end, line):
            break
        yield line
