import sys

n = int(input())
a = [int(input()) for _ in range(n)]

min_distance = sys.maxsize

for room in range(n): # 시작 방 번호
    distance = 0
    for walk in range(n): # 얼마나 이동 해야하는지
        distance += (a[(room + walk) % n] * walk)
    if distance < min_distance:
        min_distance = distance

print(min_distance)