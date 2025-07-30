n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = 101
for x in range(2, 101, 2):
    for y in range(2, 101, 2):
        cnt_1 = 0
        cnt_2 = 0
        cnt_3 = 0
        cnt_4 = 0
        for i in range(n):
            if points[i][0] > x and points[i][1] > y:
                cnt_1 += 1
            elif points[i][0] < x and points[i][1] > y:
                cnt_2 += 1
            elif points[i][0] < x and points[i][1] < y:
                cnt_3 += 1
            elif points[i][0] > x and points[i][1] < y:
                cnt_4 += 1
        
        value = max(cnt_1, cnt_2, cnt_3, cnt_4)
        answer = min(answer, value)

print(answer)