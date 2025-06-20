n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 가능한 1x3 영역의 합과 좌표를 저장
rects = []

for i in range(n):
    for j in range(n - 2):
        total = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        coords = {(i, j), (i, j + 1), (i, j + 2)}  # 셋으로 좌표 저장
        rects.append((total, coords))

max_coin = 0

# 모든 쌍 조합을 확인
for i in range(len(rects)):
    total1, coords1 = rects[i]
    for j in range(i + 1, len(rects)):
        total2, coords2 = rects[j]
        if coords1.isdisjoint(coords2):  # 두 직사각형이 겹치지 않으면
            max_coin = max(max_coin, total1 + total2)

print(max_coin)
