N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

A_ary = []
B_ary = []

# A의 이동
cur = 0
for i in range(N):
    for _ in range(t[i]):
        cur += v[i]
        A_ary.append(cur)

# B의 이동
cur = 0
for i in range(M):
    for _ in range(t2[i]):
        cur += v2[i]
        B_ary.append(cur)

cnt = 1
for i in range(1, len(A_ary)):
    if (A_ary[i-1] < B_ary[i-1]) and (A_ary[i] >= B_ary[i]):
        cnt += 1
    elif (A_ary[i-1] > B_ary[i-1]) and (A_ary[i] <= B_ary[i]):
        cnt += 1
    elif (A_ary[i-1] == B_ary[i-1]) and ((A_ary[i] < B_ary[i]) or (A_ary[i] > B_ary[i])):
        cnt += 1

print(cnt)