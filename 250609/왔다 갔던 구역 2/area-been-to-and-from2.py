n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# 충분히 넓은 선분 배열 (인덱스 범위 확보)
MAX = 20001
offset = 10000
answer = [0] * MAX

people = offset

for i in range(n):
    for _ in range(x[i]):
        # 이동 먼저
        if dir[i] == 'L':
            people -= 1
        elif dir[i] == 'R':
            people += 1

        answer[people] += 1

cnt = 0

for k in answer:
    if k >= 2:
        cnt += 1

print(cnt)