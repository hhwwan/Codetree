n = int(input())
a = list(map(int, input().split()))

max_cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        total = a[i] + a[j]
        if total % 2 != 0 :
            continue
        K = total // 2

        cnt = 0

        for x in range(n):
            for y in range(x + 1, n):
                if a[x] + a[y] == 2 * K:
                    cnt += 1
        max_cnt = max(max_cnt, cnt)
print(max_cnt)