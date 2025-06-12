N = int(input())
arr = [int(input()) for _ in range(N)]

answer = 1
cnt = 1

for i in range(1, N):
    if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
        cnt += 1
        if cnt > answer:
            answer = cnt
    # 부호가 달라진다면 초기화
    else:
        cnt = 1

print(answer)