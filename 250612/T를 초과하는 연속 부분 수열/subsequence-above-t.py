n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
answer = 0

for i in range(n):
    if arr[i] > t:
        cnt += 1
        if cnt > answer:
            answer = cnt
    else:
        cnt = 0

print(answer)