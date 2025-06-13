n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if grid[i + dx[k]][j + dy[k]] == 1:
                    cnt += 1
        if cnt >= 3:
            answer += 1

print(answer)