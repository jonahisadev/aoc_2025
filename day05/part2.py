from common import load_input
input = load_input()

ranges, _ = list(map(lambda n: n.splitlines(), list(input.split("\n\n"))))
ranges = list(map(lambda r2: [int(r2[0]), int(r2[1])], list(map(lambda r: r.split('-'), ranges))))

print("Starting Ranges:")
print(ranges)

# Sort ranges by start value
ranges.sort(key=lambda x: x[0])

merged = []
for r in ranges:
    if not merged or r[0] > merged[-1][1] + 1:
        # No overlap or adjacency - add new range
        merged.append(r[:])  # copy to avoid mutation issues
    else:
        # Overlaps or adjacent - extend the current range
        merged[-1][1] = max(merged[-1][1], r[1])

print("Final Ranges:")
print(merged)

total = 0
for mr in merged:
    total += (mr[1] - mr[0]) + 1
print(total)
