n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

place = [0] * (max(x)+1)

# 각 위치당 점수 표시
for i in range(len(x)):
    if c[i] == 'G':
        place[x[i]] = 1
    elif c[i] == 'H':
        place[x[i]] = 2

# 최대 점수 찾기
max_total = 0

for i in range(1, max(x) + 1 - k):
    tmp = 0
    for j in range(i, i + k + 1):
        tmp += place[j]
    
    if max_total < tmp:
        max_total = tmp

print(max_total)