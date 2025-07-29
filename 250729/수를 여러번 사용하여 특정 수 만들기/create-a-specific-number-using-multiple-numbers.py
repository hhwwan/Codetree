A, B, C = map(int, input().split())

max_total = 0

for i in range(C // A + 1):
    A_value = A * i
    value = C - A_value

    if value >= 0:
        j = value // B
        total = A_value + (B * j)

        if total <= C:
            max_total = max(max_total, total)

for j in range(C // B + 1):
    B_value = B * j
    value = C - B_value

    if value >= 0:
        i = value // A
        total = B_value + (A * i)

        if total <= C:
            max_total = max(max_total, total)

print(max_total)