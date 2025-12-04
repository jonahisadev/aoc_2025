from common import load_input
input = load_input()

def grid_at(grid, x, y):
    if x < 0:
        return None
    if y < 0:
        return None
    if y >= len(grid):
        return None
    if x >= len(grid[0]):
        return None

    row = grid[y]
    return row[x % len(row)]

relative = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1),
]

grid = list(map(lambda x: list(x), input.splitlines()))
w, h = len(grid[0]), len(grid)

total = 0
for y in range(h):
    for x in range(w):
        if grid_at(grid, x, y) != '@':
            continue
        res = list(map(lambda d: grid_at(grid, x + d[0], y + d[1]), relative))
        if res.count('@') < 4:
            total += 1

print(total)
