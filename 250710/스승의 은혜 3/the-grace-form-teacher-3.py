N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

gifts.sort(key=lambda x : (x[0] + x[1], -x[0]))

P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

answer = 0
for i in range(N):
    cost_list = []
    for j in range(N):
        if i == j:
            cost = P[j] // 2 + S[j]
        else:
            cost = P[j] + S[j]
        cost_list.append(cost)

    cost_list.sort()
    total = 0
    cnt = 0

    for k in cost_list:
        total += k
        if total <= B:
            cnt += 1
        else:
            break
    
    answer = max(answer, cnt)

print(answer)