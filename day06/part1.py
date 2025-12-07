from functools import reduce
import re
from common import load_input
input = load_input()
lines = input.splitlines()

# Parse rows and operations
rows = []
ops = []
pattern = r"\s*(\d+)"
for i in range(len(lines) - 1):
    line = lines[i].strip()
    res = list(map(lambda x: int(x), re.findall(pattern, line)))
    rows.append(res)
ops = re.findall(r"\S", lines[-1])

# Convert to columns
cols = [[]] * len(rows[0])
for i in range(len(rows[0])):
    col = []
    for j in range(len(rows)):
        if rows[j][i] != 0:
            col.append(rows[j][i])
    cols[i] = col

# Run calculations
total = 0
for (i, op) in enumerate(ops):
    res = 0
    if op == "*":
        res = reduce(lambda x, y: x * y, cols[i], 1)
    elif op == "+":
        res = reduce(lambda x, y: x + y, cols[i], 0)
    total += res

print(total)
