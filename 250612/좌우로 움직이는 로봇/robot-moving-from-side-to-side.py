n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

A_ary = []
B_ary = []

# A로봇
current = 0
for i in range(n):
    if d[i] == 'R':
        for _ in range(t[i]):
            current += 1
            A_ary.append(current)
    else:
        for _ in range(t[i]):
            current -= 1
            A_ary.append(current)

# B로봇
current = 0
for i in range(m):
    if d_b[i] == 'R':
        for _ in range(t_b[i]):
            current += 1
            B_ary.append(current)
    else:
        for _ in range(t_b[i]):
            current -= 1
            B_ary.append(current)

cnt = 0
end = max(len(A_ary),len(B_ary))

if len(A_ary) < end:
    A_ary += [A_ary[-1]] * (end - len(A_ary))
if len(B_ary) < end:
    B_ary += [B_ary[-1]] * (end - len(B_ary))

for i in range(1, end):
    if (A_ary[i-1] != B_ary[i-1]) and (A_ary[i] == B_ary[i]):
        cnt += 1    

print(cnt)