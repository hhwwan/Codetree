x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

answer = [[0] * 2001 for _ in range(2001)]

# A와 B 넓이 먼저 칠하기 +1
for i in range(2):
    for j in range(y1[i], y2[i]):
        for k in range(x1[i], x2[i]):
            answer[j+1000][k+1000] += 1

# M으로 덟힌곳 -1
for m in range(y1[2], y2[2]):
    for n in range(x1[2], x2[2]):
        # A와 B로 덟혀있는부분만 지우기
        if answer[m+1000][n+1000] == 1:
            answer[m+1000][n+1000] -= 1

cnt = 0

for row in answer:
    cnt += sum(row)

print(cnt)