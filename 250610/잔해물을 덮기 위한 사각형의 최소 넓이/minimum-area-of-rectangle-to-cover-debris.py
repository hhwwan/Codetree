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

length, width = 0, 0

# 세로 길이 구하기
for a in answer:
    if 1 in a:
        length += 1
# 가로 길이 구하기
for b in answer:
    if sum(b) > width:
        width = sum(b)

print(length*width)