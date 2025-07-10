k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# answer[a][b] = a가 b보다 앞선 횟수
answer = [[0] * (n + 1) for _ in range(n + 1)]

# 각 시험마다 처리
for i in range(k):
    rank = [0] * (n + 1)  # 학생 번호 → 순위 저장

    for pos, student in enumerate(arr[i]):
        rank[student] = pos

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            if rank[a] < rank[b]:
                answer[a][b] += 1

# 정답 계산: k번 모두 a가 b보다 앞선 경우만 세기
count = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            continue
        if answer[a][b] == k:
            count += 1

print(count)