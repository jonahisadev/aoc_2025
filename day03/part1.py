from common import load_input
input = load_input()

def find_largest(batteries: [int], start_index: int, chop: int) -> int:
    largest = -1
    largest_index = -1
    for i in range(start_index, len(batteries) - chop):
        if batteries[i] > largest:
            largest = batteries[i]
            largest_index = i
    return largest_index

total = 0
banks = input.split('\n')
for bank in banks:
    batteries = list(map(int, list(bank)))
    a = find_largest(batteries, 0, 1)
    b = find_largest(batteries, a + 1, 0)
    total += (batteries[a] * 10) + batteries[b]

print(total)
