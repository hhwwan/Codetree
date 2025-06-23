n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
for i in range(n - k + 1):
    tmp = 0
    for j in range(i, i + k):
        tmp += arr[j]

    if answer < tmp:
        answer = tmp

print(answer)