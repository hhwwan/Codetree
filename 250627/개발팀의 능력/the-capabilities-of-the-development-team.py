from itertools import combinations

arr = list(map(int, input().split()))

min_value = float('inf')
found = False

# 5명 중 2명 먼저 team1로 선택
for team1 in combinations(range(5), 2):
    remain_people = [i for i in range(5) if i not in team1]

    # 남은 3명 중 2명 고르기
    for team2 in combinations(remain_people, 2):
        team3 = [i for i in remain_people if i not in team2]

        sum1 = arr[team1[0]] + arr[team1[1]]
        sum2 = arr[team2[0]] + arr[team2[1]]
        sum3 = arr[team3[0]]

        if sum1 != sum2 and sum1 != sum3 and sum2 != sum3:
            found = True
            min_value = min(min_value, (max(sum1, sum2, sum3) - min(sum1, sum2, sum3)))

if found:
    print(min_value)
else:
    print(-1)