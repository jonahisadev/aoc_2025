from common import load_input
input = load_input()

ranges, ids = list(map(lambda n: n.splitlines(), list(input.split("\n\n"))))
ids = list(map(lambda i: int(i), ids))
ranges = list(map(lambda r2: [int(r2[0]), int(r2[1])], list(map(lambda r: r.split('-'), ranges))))

# print(ranges)
# print(ids)

total = 0
for _id in ids:
    for r in ranges:
        if r[0] <= _id <= r[1]:
            total += 1
            break
print(total)
