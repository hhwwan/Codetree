import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = sys.maxsize

for i in range(N-1):
    for j in range(i+1, N):
        if answer > abs(S - (sum(arr) - (arr[i] + arr[j]))):
            answer = abs(S - (sum(arr) - (arr[i] + arr[j])))

print(answer)