n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

max_cnt = 0
answer = 0
for i in range(3):
    cup = [0,0,0]
    cup[i] = 1
    cnt = 0

    for j in range(n):      
        cup[a[j]-1], cup[b[j]-1] = cup[b[j]-1], cup[a[j]-1]
        if cup[c[j]-1] == 1:
            cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)