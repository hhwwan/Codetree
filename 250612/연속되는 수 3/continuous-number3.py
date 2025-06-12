N = int(input())
arr = [int(input()) for _ in range(N)]

answer = 0
pos = 0 # 양수
neg = 0 # 음수

for i in range(N):
    if (i == 0 and arr[i] < 0) or (arr[i-1] > 0 and arr[i] < 0):
        neg += 1
    elif (i == 0 and arr[i] > 0) or (arr[i-1] < 0 and arr[i] > 0):
        pos += 1
    elif arr[i-1] < 0 and arr[i] < 0:
        pos = 0
        neg += 1
        if neg > answer:
            answer = neg
    elif arr[i-1] > 0 and arr[i] > 0:
        neg = 0
        pos += 1
        if pos > answer:
            answer = pos

print(answer)