n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

MAX_R = 2000
OFFSET = 1000

current = 0
start_positions = []
end_positions = []

for i in range(n):
    distance = x[i]
    direction = dir[i]

    if direction == 'L':
        start = current - distance
        end = current
        current -= distance
    else:
        start = current
        end = current + distance
        current += distance

    start += OFFSET
    end += OFFSET

    start_positions.append(start)
    end_positions.append(end)

checked = [0] * (MAX_R + 1)

for i in range(n):
    for pos in range(start_positions[i], end_positions[i]):
        checked[pos] += 1

result = 0
for count in checked:
    if count >= 2:
        result += 1

print(result)