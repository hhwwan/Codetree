N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
cnt = 0
found = False

for i in range(N):
    for j in range(dist[i]):
        if dir[i] == 'N': # 위
            nx, ny = x + dx[0], y + dy[0]
        elif dir[i] == 'E': # 오른쪽
            nx, ny = x + dx[1], y + dy[1]
        elif dir[i] == 'S': # 아래
            nx, ny = x + dx[2], y + dy[2]
        elif dir[i] == 'W': # 왼쪽
            nx, ny = x + dx[3], y + dy[3]
        
        x, y = nx, ny
        cnt += 1

        if x == 0 and y == 0:
            print(cnt)
            found = True
            break
    
    if found:
        break

if not found:
    print(-1)