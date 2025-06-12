n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 1
answer = 1

for i in range(1, n):
    if arr[i] > arr[i-1]:
        cnt += 1
        if cnt > answer:
            answer = cnt
    else:
        cnt = 1

print(answer)