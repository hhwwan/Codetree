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

for time, a, b in sort_hand:
    # 첫번째 개발자가 감염자 + 전염가능횟수 남음
    if answer[a-1] == 1 and virus[a] > 0:
        # 두번째 개발자가 감염당한적이 없는 경우
        if answer[b-1] == 0:
            answer[b-1] = 1
            virus[b] = K
        # 두번째 개발자도 이미 감염자인 경우 -> 아무것도 안해도 됨

        # 전염 가능 횟수 -1
        virus[a] -= 1
    # 첫번째 개발자가 감염자 + 전염가능횟수 없음 -> 아무것도 안해도 됨

    # 두번째 개발자가 감염자 + 감염가능횟수 남음
    if answer[b-1] == 1 and virus[b] > 0:
        # 첫번째 개발자가 감염당한적인 없는 경우
        if answer[a-1] == 0:
            answer[a-1] = 1
            virus[a] = K
        # 첫번째 개발자가 이미 감염자인 경우 -> 아무것도 안해도 됨

        # 전염 가능 횟수 -1
        virus[b] -= 1

for i in answer:
    print(i, end='')   