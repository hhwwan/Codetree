import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

answer = sys.maxsize

for i in range(n):
    extent = 0 # 넓이
    min_x = 40000
    max_x = 0
    min_y = 40000
    max_y = 0
    for j in range(n):
        if i == j:
            continue
        
        min_x = min(min_x, x[j])
        max_x = max(max_x, x[j])
        min_y = min(min_y, y[j])
        max_y = max(max_y, y[j])

    width = max_x - min_x
    height = max_y - min_y

    extent = width * height

    answer = min(answer, extent)

print(answer)