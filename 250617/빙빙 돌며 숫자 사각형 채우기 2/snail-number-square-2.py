n, m = map(int, input().split())

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0
dir_num = 0 # 아래, 오른쪽, 위, 왼쪽

arr = [[0] * m for _ in range(n)]
arr[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dx[dir_num], y + dy[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()