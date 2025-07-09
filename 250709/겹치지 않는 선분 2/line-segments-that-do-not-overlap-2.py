n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

def cross(a, b):
    return (a[0] < b[0] and a[1] > b[1]) or (a[0] > b[0] and a[1] < b[1])

answer = 0
for i in range(n):
    found = False
    for j in range(n):
        if i == j:
            continue
        if cross(lines[i], lines[j]):
            found = True
            break
    if not found:
        answer += 1

print(answer)