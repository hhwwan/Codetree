A, B, C = map(int, input().split())

max_total = 0
for i in range(C // (A + 1)):
    A_value = A * i
    value = C - A_value

    j = value // (B + 1)
    total = A_value + (B * j)

    max_total = max(max_total, total)

print(max_total)