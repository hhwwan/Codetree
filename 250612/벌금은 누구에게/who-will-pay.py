N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

penalty = [K] * (N + 1) # 0번째꺼 안씀
answer = 0

for i in range(M):
    penalty[student[i]] -= 1
    if penalty[student[i]] == 0:
        answer = student[i]
        break

if answer:
    print(answer)
else:
    print(-1)