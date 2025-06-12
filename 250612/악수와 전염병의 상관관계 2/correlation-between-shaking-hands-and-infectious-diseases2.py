from collections import defaultdict

N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# 시간 순으로 정렬
sort_hand = sorted(handshakes, key = lambda x : x[0])
# {번호:전염 가능 횟수} 로 딕셔너리 생성
virus = {i: 0 for i in range(1,N+1)}
# 전염 여부
answer = [0] * N
# 초기 바이러스 감염자 설정
answer[P-1] = 1
virus[P] = K

# 시간별로 묶기
time_map = defaultdict(list)
for t, a, b in sort_hand:
    time_map[t].append((a, b))

# 시간순으로 처리
for t in sorted(time_map.keys()):
    today = time_map[t]

    # 전염 시도 전에 현재 감염 상태 저장 (동시간 감염 방지)
    infected_now = set()

    for a, b in today:
        if answer[a - 1] == 1 and virus[a] > 0:
            infected_now.add((a, b))
        if answer[b - 1] == 1 and virus[b] > 0:
            infected_now.add((b, a))
        
    # 전염 처리
    for a, b in infected_now:
        if answer[b - 1] == 0:
            answer[b - 1] = 1
            virus[b] = K
        virus[a] -= 1

for i in answer:
    print(i, end='')   