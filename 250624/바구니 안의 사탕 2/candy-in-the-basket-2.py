N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# 위치에 사탕 채우기
arr = [0] * (100 + K + 1)

for i in range(N):
    arr[pos[i]] += candy[i]

# c 찾기
max_candy = 0

for c in range(len(arr)):
    left = max(0, c - K)
    right = min(len(arr) - 1, c + K)
    
    tmp = 0
    for j in range(left, right + 1):
        tmp += arr[j]
    if max_candy < tmp:
        max_candy = tmp

print(max_candy)