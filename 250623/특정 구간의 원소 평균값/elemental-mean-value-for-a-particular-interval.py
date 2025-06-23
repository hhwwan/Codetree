n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += arr[j]
        if (tmp / (j - i + 1)) in arr[i:j+1]:
            cnt += 1

print(cnt)