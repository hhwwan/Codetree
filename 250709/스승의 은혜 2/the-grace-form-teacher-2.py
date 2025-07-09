N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

P.sort()

total = 0
cnt = 0
for cost in P:
    total += cost
    if total <= B:
        cnt += 1
    else:
        total -= cost
        total += (cost // 2)
        if total <= B:
            cnt += 1
            break
        else:
            break

print(cnt)