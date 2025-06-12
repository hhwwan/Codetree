n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0
answer = 0

for i in range(n):
    if i == 0 or arr[i] == arr[i-1]:
        cnt += 1
        # 연속된 수가 최대값인지 확인
        if cnt > answer:
            answer = cnt
    # 동일한 숫자가 아니라면 카운트 1로 초기화
    else:
        cnt = 1

print(answer)