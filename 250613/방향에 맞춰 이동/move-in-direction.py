n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for i in range(len(dir)):
    for _ in range(dist[i]):
        if dir[i] == 'E':
            nx, ny = x + dx[0], y + dy[0]
        elif dir[i] == 'S':
            nx, ny = x + dx[1], y + dy[1]
        elif dir[i] == 'W':
            nx, ny = x + dx[2], y + dy[2]
        elif dir[i] == 'N':
            nx, ny = x + dx[3], y + dy[3]

        x, y = nx, ny

print(x, y)