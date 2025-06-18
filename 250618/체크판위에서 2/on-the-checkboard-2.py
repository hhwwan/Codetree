R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

cnt = 0
start = grid[0][0]
end = grid[R-1][C-1]

for i in range(1, R-1):
    for j in range(1, C-1):
        # 첫번째 점프 지점
        if grid[i][j] == start:
            continue
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):
                if grid[k][l] == grid[i][j]:
                    continue
                if grid[k][l] != end:
                    cnt += 1

print(cnt)