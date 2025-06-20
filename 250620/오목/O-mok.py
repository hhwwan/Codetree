board = [list(map(int, input().split())) for _ in range(19)]

directions = [
    (0, 1),
    (1, 0),
    (1, 1),
    (-1, 1)
]

def check(x, y):
    stone = board[x][y]

    if stone == 0:
        return None

    for dx, dy in directions:
        cnt = 1
        nx, ny = x, y
        pos = [(x, y)]

        while True:
            nx += dx
            ny += dy
            if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == stone:
                cnt += 1
                pos.append((nx, ny))
            else:
                break

        if cnt == 5:
            mid_x, mid_y = pos[2]

            return stone, mid_x + 1, mid_y + 1
    
    return None

found = False

for i in range(19):
    for j in range(19):
        result = check(i, j)
        if result:
            print(result[0])
            print(result[1], result[2])
            found = True
            break
    if found:
        break

if not found:
    print(0)