N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

boom = -1
for i in range(N - K):
    for j in range(i+1, N):
        if num[i] == num[j]:
            boom = max(boom, num[i])

print(boom)