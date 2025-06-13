dirs = input()

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3 # 북쪽

for i in dirs:
    if i == 'L':
        dir_num = (dir_num - 1) % 4
    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    elif i == 'F':
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        x, y = nx, ny

print(x, y)