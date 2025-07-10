n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

lines = [0] * (max(r) + 1)
cnt = 0

# 선분이 있는 곳 채우기
for i in range(n):
    for j in range(l[i], r[i] + 1):
        lines[j] += 1

# 선분 3개씩 빼기
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            # 원본 배열 복사
            temp = lines[:]

            for a in range(l[k], r[k] + 1):
                temp[a] -= 1
            for b in range(l[j], r[j] + 1):
                temp[b] -= 1
            for c in range(l[i], r[i] + 1):
                temp[c] -= 1
            
            found = True
            
            for x in temp:
                if x >= 2:
                    found = False
                    break
            
            if found:
                cnt += 1

print(cnt)