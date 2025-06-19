n = int(input())
numbers = list(map(int, input().split()))

max_total = 0
for i in range(n):
    for j in range(i+2, n):
        total = numbers[i] + numbers[j]
        if total > max_total:
            max_total = total

print(max_total)