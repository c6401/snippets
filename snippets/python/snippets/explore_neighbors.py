visited = set()

def dfs(x, y):
    if (x, y) in visited:
        return

    visited.add((x, y))
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        dfs(x + dx, y + dy)
