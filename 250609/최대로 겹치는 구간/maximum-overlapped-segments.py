n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

answer = [0] * 201

for i in segments:
    for j in range(i[0], i[1]+1):
        answer[j+100] += 1

print(max(answer))