N, M = map(int, input().split())
arr = [input() for _ in range(N)]

directions = [
    (0, 1), # 오른쪽
    (0, -1), # 왼쪽
    (-1, 0), # 위
    (1, 0), # 아래
    (1, 1), # 오른 대각선 밑
    (-1, 1), # 오른 대각선 위
    (-1, -1), # 왼 대각선 위
    (1, -1) # 왼 대각선 아래
]

def check(x, y):
    word = arr[x][y]

    if word == 'L':
        cnt = 0
        for dx, dy in directions:
            nx, ny = x, y
            found = False
            for _ in range(2):
                nx += dx
                ny += dy
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 'E':
                    found = True
                    pass
                else:
                    found = False
                    break
            if found:
                cnt += 1
        return cnt
    return None

answer = 0
for i in range(N):
    for j in range(M):
        result = check(i, j)
        if result:
            answer += result

print(answer)