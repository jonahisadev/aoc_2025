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

    allowed = 12
    last_index = 0
    for i in range(allowed):
        n = find_largest(batteries, last_index, (allowed - i - 1))
        power = pow(10, (allowed - i - 1))
        total += batteries[n] * (1 if power == 0 else power)
        last_index = n + 1

print(total)
