def neightbours_on_grid(row, col, rows, cols):
    if col > 0:
        yield (row, col - 1)
    if row > 0:
        yield (row - 1, col)
    if col + 1 < cols:
        yield (row, col + 1)
    if row + 1 < rows:
        yield (row + 1, col)
