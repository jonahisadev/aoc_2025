from common import load_input
input = load_input()

def has_pattern_count(s, m, k):
    if s.count(s[:m]) >= k:
        return True
    return False

def id_is_invalid(prod_id: int) -> bool:
    # Single digit IDs can't possibly match the criteria
    # And yes, this got me
    if prod_id < 10:
        return False

    str_id = str(prod_id)
    str_len = len(str_id)

    # m -> pattern length
    # k -> number of repetitions
    # m * k should always equal str_len
    # i.e., str_len / m should always be a whole number, and the result is k

    m = 1
    while m < (str_len / 2) + 1:
        if str_len % m == 0:
            k = str_len / m
            if has_pattern_count(str_id, m, k):
                return True
        m += 1

    return False

# Gross, but it works
ranges = list(map(lambda x: list(map(lambda y: int(y), x.split('-'))), input.split(',')))
counter = 0

# Dumb solution but it works
for r in ranges:
    print("Processing range:", r)
    for prod_id in range(r[0], r[1] + 1):
        if id_is_invalid(prod_id):
            counter += prod_id

print(counter)
