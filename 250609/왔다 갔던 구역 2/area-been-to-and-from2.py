n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# 충분히 넓은 선분 배열 (인덱스 범위 확보)
MAX = 20001
people = 10000
answer = [0] * MAX

for i in range(n):
    if dir[i] == 'L':
        for _ in range(x[i]):
            people -= 1
            answer[people] += 1
    elif dir[i] == 'R':
        for _ in range(x[i]):
            people += 1
            answer[people] += 1

cnt = 0

for k in answer:
    if k >= 2:
        cnt += 1

print(cnt)