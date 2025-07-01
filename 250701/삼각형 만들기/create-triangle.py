n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

triangle_distance = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, x2, x3 = x[i], x[j], x[k]
            y1, y2, y3 = y[i], y[j], y[k]

            extent = 0

            if y1 == y2 and x2 == x3:
                extent = abs(x1 - x2) * abs(y2 - y3)
            
            elif y2 == y3 and x3 == x1:
                extent = abs(x2 - x3) * abs(y3 - y1)
            
            elif y3 == y1 and x1 == x2:
                extent = abs(x3 - x1) * abs(y1 - y2)
        
            triangle_distance = max(triangle_distance, extent)

if triangle_distance:
    print(triangle_distance)
else:
    print(0)