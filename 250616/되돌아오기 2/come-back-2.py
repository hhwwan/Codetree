commands = input()

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3 # 오른쪽, 아래, 왼쪽, 위
sec = 0
found = False

for i in range(len(commands)):
    if commands[i] == 'F':
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        x ,y = nx, ny
        sec += 1
        if x == 0 and y == 0:
            print(sec)
            found = True
            break
    elif commands[i] == 'L':
        dir_num = (dir_num - 1) % 4
        sec += 1
    elif commands[i] == 'R':
        dir_num = (dir_num + 1) % 4
        sec += 1

if not found:
    print(-1)