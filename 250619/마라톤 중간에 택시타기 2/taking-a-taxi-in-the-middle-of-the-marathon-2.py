import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_distance = sys.maxsize

for i in range(n-2):
    num = 1
    distance = 0
    start_x = x[0]
    start_y = y[0]
    for j in range(1, n-1):
        if j == num:
            continue
        distance += (abs(x[j]-start_x) + abs(y[j]-start_y))
        start_x = x[j]
        start_y = y[j]
    distance += (abs(start_x - x[-1]) + abs(start_y - y[-1]))
    if distance < min_distance:
        min_distance = distance
    num += 1

print(min_distance)