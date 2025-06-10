n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

answer = [[0] * 201 for _ in range(201)]

for i in range(n):
    # 빨간색일때
    if i == 0 or i % 2 == 0:
        for j in range(y1[i],y2[i]):
            for k in range(x1[i],x2[i]):
                answer[j+100][k+100] = 1
    # 파란색일때
    else:
        for j in range(y1[i],y2[i]):
            for k in range(x1[i],x2[i]):
                answer[j+100][k+100] = 2

cnt = 0

for row in answer:
    cnt += row.count(2)
print(cnt)