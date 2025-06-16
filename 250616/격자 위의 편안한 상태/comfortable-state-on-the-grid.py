n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 아래, 왼쪽, 위, 오른쪽 
arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = points[i]
    arr[x][y] = 1 # 색칠
    cnt = 0

    for j in range(4):
        if 0 <= x + dx[j] <= n and 0 <= y + dy[j] <= n:
            if arr[x+dx[j]][y+dy[j]] == 1:
                cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)