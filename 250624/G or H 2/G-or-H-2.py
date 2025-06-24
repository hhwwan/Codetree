n = int(input())
people = [tuple(input().split()) for _ in range(n)]
people.sort(key = lambda x : int(x[0])) # 추가
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

max_len = 0

for i in range(len(alpha)): # 시작 위치
    G_cnt = 0
    H_cnt = 0
    for j in range(i, len(alpha)):
        if alpha[j] == 'G':
            G_cnt += 1
        elif alpha[j] == 'H':
            H_cnt += 1
        
        if (G_cnt != 0 and H_cnt == 0) or (G_cnt == 0 and H_cnt != 0) or (G_cnt == H_cnt):
            tmp = pos[j] - pos[i]
            if tmp > max_len:
                max_len = tmp

print(max_len)