n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

from itertools import combinations

# x축 3개로 가능한지
for comb in combinations(x, 3):
    if all(x in comb for x, y in points):
        print(1)
        exit()

# y축 3개로 가능한지
for comb in combinations(y, 3):
    if all(y in comb for x, y in points):
        print(1)
        exit()

# x축 2개 + y축 1개
for x1, x2 in combinations(x, 2):
    remain = [(x, y) for x, y in points if x != x1 and x != x2]
    y_set = set(y for x, y in remain) # 중복 제거해서 1개 이상이면 어짜피 실패
    if len(y_set) <= 1:
        print(1)
        exit()

# x축 1개 + y축 2개
for x1 in x:
    remain = [(x, y) for x, y in points if x != x1]
    y_set = set(y for x, y in remain)
    if len(y_set) <= 2:
        print(1)
        exit()

# y축 2개 + x축 1개
for y1, y2 in combinations(y, 2):
    remain = [(x, y) for x, y in points if y != y1 and y != y2]
    x_set = set(x for x, y in remain)
    if len(x_set) <= 1:
        print(1)
        exit()

# y축 1개 + x축 2개
for y1 in y:
    remain = [(x, y) for x, y in points if y != y1]
    x_set = set(x for x, y in remain)
    if len(x_set) <= 2:
        print(1)
        exit()

print(0)