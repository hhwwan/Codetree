n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

max_time = 0

for i in range(n):
    ing = [0] * (max(b) + 1)
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        
        for k in range(a[j], b[j]):
            ing[k] += 1

    for x in ing:
        if x:
            cnt += 1
    max_time = max(max_time, cnt)

print(max_time)