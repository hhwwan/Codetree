n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

A_ary = []
B_ary = []
A_current = 0
B_current = 0

for i in range(n):
    if d[i] == 'R':
        for j in range(t[i]):
            A_current += 1
            A_ary.append(A_current)
    else:
        for j in range(t[i]):
            A_current -= 1
            A_ary.append(A_current)

for i in range(m):
    if d2[i] == 'R':
        for j in range(t2[i]):
            B_current += 1
            B_ary.append(B_current)
    else:
        for j in range(t2[i]):
            B_current -= 1
            B_ary.append(B_current)

answer = 0
for k in range(min(len(A_ary),len(B_ary))):
    if A_ary[k] == B_ary[k]:
        answer = k + 1
        break

if answer:
    print(answer)
else:
    print(-1) 