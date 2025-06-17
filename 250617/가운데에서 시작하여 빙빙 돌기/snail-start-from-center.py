n = int(input())
grid = [[0] * n for _ in range(n)]

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
x, y = n // 2, n // 2
dir_num = 0 # 오른쪽, 위, 왼쪽, 아래 

grid[x][y] = 1
num = 2
step = 1 # 이동할 칸 수

while num <= n * n:
    for _ in range(2):
        for _ in range(step):
            nx, ny = x + dx[dir_num], y + dy[dir_num]

            if 0 <= nx < n and 0 <= ny < n:
                x, y = nx, ny
                grid[x][y] = num
                num += 1
                if num > n * n:
                    break
        if num > n * n:
            break
        dir_num = (dir_num + 1) % 4
    step += 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()