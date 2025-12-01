from common import load_input
input = load_input()
lines = input.split('\n')

tick = 50
count = 0

for line in lines:
    direction = -1 if line[0] == 'L' else 1
    steps = int(line[1:])
    delta = direction * steps

    lastTick = tick
    tick += delta

    div = tick // 100
    remainder = tick % 100

    # Count full laps
    count += abs(div)

    # Prevent double counting when starting at 0
    if lastTick == 0 and div < 0:
        count -= 1

    # Count if we land exactly on 0 going down without going over
    if remainder == 0 and delta < 0:
        count += 1

    # Reset tick
    tick = remainder

print(count)
