n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

A_ary = []
B_ary = []

# A의 움직임
current = 0
for i in range(n):
    for _ in range(t[i]):
        current += v[i]
        A_ary.append(current)

# B의 움직임
current = 0 # 0으로 초기화
for i in range(m):
    for _ in range(t2[i]):
        current += v2[i]
        B_ary.append(current)

prev_leader = 'draw'
cnt = 0

for i in range(len(A_ary)):
    if A_ary[i] > B_ary[i]:
        leader = 'A'
    elif A_ary[i] < B_ary[i]:
        leader = 'B'
    else:
        leader = 'draw'
    
    # 선두가 바뀐경우(같을 때 제외)
    if leader != prev_leader and leader != 'draw' and prev_leader != 'draw':
        cnt += 1
        prev_leader = leader
    # 최초 리더 설정 (draw -> A or B) 시에는 갱신만
    elif prev_leader == 'draw' and leader != 'draw':
        prev_leader = leader
print(cnt)