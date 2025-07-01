n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

max_area = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
                continue

            x1, y1 = x[i], y[i]
            x2, y2 = x[j], y[j]
            x3, y3 = x[k], y[k]

            area = 0

            if y1 == y2 and x1 == x3 and y3 != y1 and x3 != x2:
                area = abs(x1 - x2) * abs(y1 - y3)
                max_area = max(max_area, area)
            elif y2 == y3 and x2 == x1 and y1 != y2 and x1 != x3:
                area = abs(x2 - x3) * abs(y2 - y1)
                max_area = max(max_area, area)
            elif y3 == y1 and x3 == x2 and y2 != y3 and x2 != x1:
                area = abs(x3 - x1) * abs(y3 - y2)
                max_area = max(max_area, area)

if max_area:
    print(max_area)
else:
    print(0)