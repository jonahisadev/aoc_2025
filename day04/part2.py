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

while True:
    to_remove = []
    local_total = 0
    for y in range(h):
        for x in range(w):
            if grid_at(grid, x, y) != '@':
                continue
            res = list(map(lambda d: grid_at(grid, x + d[0], y + d[1]), relative))
            if res.count('@') < 4:
                to_remove.append((x, y))
                local_total += 1
    if local_total == 0:
        break
    total += local_total
    for (x, y) in to_remove:
        grid[y][x] = '.'

print(total)
