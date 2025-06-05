n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

points.sort(key=lambda x : (abs(x[1][0]) + abs(x[1][1]), x[0]))

for i in range(n):
    print(points[i][0] + 1)