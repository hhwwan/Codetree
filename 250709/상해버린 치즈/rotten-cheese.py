N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

max_sick = 0

for cheese in range(1, M+1): # 치즈 번호 순서대로
    possible = True

    # 아픈 사람들은 이 치즈를 아프기 전에 먹었는지 확인
    for i in range(S):
        found = False

        for j in range(D):
            if p[j] == sick_p[i] and m[j] == cheese and t[j] < sick_t[i]:
                found = True
                break

        if not found:
            possible = False
            break

    if not possible:
        continue
    
    # 건강하면 이 치즈를 안먹었거나 아픈 사람보다 늦게 먹어야함
    for k in range(D):
        if m[k] != cheese:
            continue
        if p[k] in sick_p:
            idx = sick_p.index(p[k])
            if t[k] < sick_t[idx]:  # 아프기 전에 먹은 것 → 문제 없음
                continue
            else:
                # 아프고 나서 먹은 것 → 상관 없음
                continue
        else:
            # 안 아픈 사람이 먹었으면 일단 정상 치즈
            possible = False
            break
        
    if not possible:
        continue
    
    # 해당 치즈가 상했을 가능성 있음
    cnt = 0
    for l in range(D):
        if m[l] == cheese:
            cnt += 1
    
    max_sick = max(max_sick, cnt)

print(max_sick)