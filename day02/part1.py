from common import load_input
input = load_input()

# There's gotta be a better way to do this
def id_is_invalid(prod_id: int) -> bool:
    str_id = str(prod_id)
    if len(str_id) % 2 != 0:
        return False
    mid = int(len(str_id) / 2)
    first, last = str_id[:mid], str_id[mid:]
    return first == last

# Gross, but it works
ranges = list(map(lambda x: list(map(lambda y: int(y), x.split('-'))), input.split(',')))
counter = 0

# Dumb solution but it works
for r in ranges:
    for prod_id in range(r[0], r[1] + 1):
        if id_is_invalid(prod_id):
            counter += prod_id

print(counter)
