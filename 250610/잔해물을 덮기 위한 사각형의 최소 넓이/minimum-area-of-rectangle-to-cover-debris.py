x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())


answer = [[0] * 2001 for _ in range(2001)]

# 첫번째 직사각형 칠하기
for i in range(y1[0], y2[0]):
    for j in range(x1[0], x2[0]):
        answer[i+1000][j+1000] += 1

# 두번째 직사각형 있는곳 지우기
for i in range(y1[1], y2[1]):
    for j in range(x1[1], x2[1]):
        # 이미 덟혀있는부분만 지우기
        if answer[i+1000][j+1000] == 1:
            answer[i+1000][j+1000] -= 1

min_x, max_x = 2001, -1
min_y, max_y = 2001, -1

# 가로, 세로 길이 구하기
for i in range(2001):
    for j in range(2001):
        if answer[i][j] == 1:
            min_y = min(min_y, i)
            max_y = max(max_y, i)
            min_x = min(min_x, j)
            max_x = max(max_x, j)

if min_x == 2001:
    print(0)
else:
    height = max_y - min_y + 1
    width = max_x - min_x + 1

print(height * width)