N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# 위치에 사탕 채우기
arr = [0] * (max(pos) + 1)

for i in range(N):
    arr[pos[i]] = candy[i]

# c 찾기
max_candy = 0

for c in range(K + 1, max(pos) + 1 - K):
    tmp = 0
    for j in range(c - K, c + K + 1):
        tmp += arr[j]
    if tmp > max_candy:
        max_candy = tmp

print(max_candy)