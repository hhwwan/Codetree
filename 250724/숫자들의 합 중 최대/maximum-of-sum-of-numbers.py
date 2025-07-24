X, Y = map(int, input().split())

max_num = 0
for i in range(X, Y + 1):
    total = sum(tuple(map(int, str(i))))
    max_num = max(max_num, total)

print(max_num)