n = int(input())
h = [int(input()) for _ in range(n)]

max_cnt = 0
for height in range(min(h) + 1, max(h)):
    cnt = 0
    for i in range(n-1):
        if h[i] - height > 0 and h[i+1] - height <= 0:
            cnt += 1
    if h[n-1] - height > 0:
        cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)