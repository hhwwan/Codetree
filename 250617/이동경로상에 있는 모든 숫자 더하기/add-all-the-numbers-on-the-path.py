N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y = N // 2, N // 2
dir_num = 0 # 위, 오른쪽, 아래, 왼쪽
cnt = board[x][y]

for i in str:
    if i == 'R':
        dir_num = (dir_num + 1) % 4
    elif i == 'L':
        dir_num = (dir_num - 1) % 4
    else:
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if 0 <= nx < N and 0 <= ny < N:
            x, y = nx, ny
            cnt += board[x][y]

print(cnt)