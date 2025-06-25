N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def near(x):
    res = []
    for i in [-2, -1, 0, 1, 2]:
        val = (x + i - 1) % N + 1
        res.append(val)
    return res

def combination(a, b, c):
    comb = set()
    for i in near(a):
        for j in near(b):
            for k in near(c):
                comb.add((i, j, k))
    return comb

set1 = combination(a1, b1, c1)
set2 = combination(a2, b2, c2)

result = len(set1.union(set2))

print(result)