arr = list(map(int, input().split()))

min_value = float('inf')

for i in range(5):
    team1, team2, team3 = 0, 0, 0

    team1 = arr[i]
    for j in range(5):
        if j == i:
            continue
        else:
            team2 = arr[j]
        for k in range(5):
            if k == i or k == j:
                continue
            else:
                team2 += arr[k]
            team3 = sum(arr) - (team1 + team2)

            if team1 != team2 and team1 != team3 and team2 != team3:
                value = max(team1, team2, team3) - min(team1, team2, team3)
                min_value = min(min_value, value)

if min_value != 0:
    print(min_value)
else:
    print(-1)