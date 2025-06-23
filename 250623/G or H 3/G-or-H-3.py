n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

place = []

# 각 위치당 점수 표시
for i in range(n):
    if c[i] == 'G':
        score = 1
    elif c[i] == 'H':
        score = 2
    place.append((x[i], score))

place.sort()

# 최대 점수 찾기
left = 0
right = 0
total = 0
max_total = 0

for right in range(n):
    total += place[right][1]
    while place[right][0] - place[left][0] > k:
        total -= place[left][1]
        left += 1
    if total > max_total:
        max_total = total

print(max_total)