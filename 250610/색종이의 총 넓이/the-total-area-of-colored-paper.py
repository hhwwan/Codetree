n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

answer = [[0] * 201 for _ in range(201)]

for i in range(3):
    for j in range(y[i],y[i]+8):
        for k in range(x[i],x[i]+8):
            if answer[j+100][k+100] == 0:
                answer[j+100][k+100] += 1

cnt = 0

for row in answer:
    cnt += sum(row)
print(cnt)