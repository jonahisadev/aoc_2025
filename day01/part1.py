from common import load_input
input = load_input()
lines = input.split('\n')

tick = 50
count = 0

for line in lines:
    direction = -1 if line[0] == 'L' else 1
    steps = int(line[1:])
    delta = direction * steps

    tick += delta
    while tick >= 100:
        tick -= 100
    while tick < 0:
        tick += 100

    if tick == 0:
        count += 1

print(count)
