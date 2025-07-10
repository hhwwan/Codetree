N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

boom = -1
for i in range(N - 1):
    for j in range(i + 1, i + 1 + K):
        if j < N:
            if num[i] == num[j]:
                boom = max(boom, num[i])

print(boom)