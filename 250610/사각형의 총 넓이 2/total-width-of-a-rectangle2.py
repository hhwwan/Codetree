n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

answer = [[0] * 201 for _ in range(201)]

for a in range(n):
    for i in range(y1[a], y2[a]):
        for j in range(x1[a], x2[a]):
            if answer[i+100][j+100] == 0:
                answer[i+100][j+100] += 1

cnt = 0

for row in answer:
    cnt += sum(row)
print(cnt)