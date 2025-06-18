import sys

n = int(input())
A = list(map(int, input().split()))

min_distance = sys.maxsize

for i in range(n):
    distance = 0
    for j in range(n):
        distance += (A[j] * abs(i-j))
    if distance < min_distance:
        min_distance = distance

print(min_distance)