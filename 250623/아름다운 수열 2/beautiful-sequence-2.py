N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
cnt = 0
for i in range(N - M + 1):
    tmp = sorted(A[i:i+M])
    if tmp == B:
        cnt += 1

print(cnt)