T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

def distance(num):
    dis_S = 1000
    dis_N = 1000
    for i in range(T):
        if c[i] == 'S':
            dis_S = min(dis_S, abs(x[i] - num))
        elif c[i] == 'N':
            dis_N = min(dis_N, abs(x[i] - num))
    
    if dis_S <= dis_N:
        return 1
    return 0

answer = 0
for num in range(a, b + 1):
    answer += distance(num)

print(answer)