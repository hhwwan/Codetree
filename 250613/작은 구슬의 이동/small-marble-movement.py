n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(t):
    if d == 'R':
        dir_idx = 0
    elif d == 'L':
        dir_idx = 1
    elif d == 'S':
        dir_idx = 2
    elif d == 'N':
        dir_idx = 3

    nx = r + dx[dir_idx]
    ny = c + dy[dir_idx]
    
    # 범위안에 있으면 진행
    if 1 <= nx <= n and 1 <= ny <= n:
        r, c = nx, ny
    # 벽에 부딪히면 방향 바꾸기
    else:
        if d == 'R':
            d = 'L'
        elif d == 'L':
            d = 'R'
        elif d == 'S':
            d = 'N'
        elif d == 'N':
            d = 'S'

print(r, c)