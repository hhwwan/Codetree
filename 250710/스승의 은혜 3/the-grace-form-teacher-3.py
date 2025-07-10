N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

gifts.sort(key=lambda x : x[0] + x[1])

P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

total = 0
cnt = 0
for i in range(N):
    total += P[i]
    total += S[i]
    if total < B:
        cnt += 1
    else:
        total -= (P[i] // 2)
        if total < B:
            cnt += 1
            break

print(cnt)