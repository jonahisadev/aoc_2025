from functools import reduce
import re
from common import load_input
input = load_input()
lines = input.splitlines()

# Parse rows
rows = []
lines_to_proc = len(lines) - 1
curr_row = []
for i in range(len(lines[0])):
    string_builder = ""
    for j in range(lines_to_proc):
        string_builder += lines[j][i]
    if string_builder.strip() != "":
        curr_row.append(int(string_builder))
    else:
        rows.append(curr_row)
        curr_row = []
rows.append(curr_row)

# Parse operations
ops = []
ops = re.findall(r"\S", lines[-1])

# Run calculations
total = 0
for (i, op) in enumerate(ops):
    res = 0
    if op == "*":
        res = reduce(lambda x, y: x * y, rows[i], 1)
    elif op == "+":
        res = reduce(lambda x, y: x + y, rows[i], 0)
    total += res

print(total)
