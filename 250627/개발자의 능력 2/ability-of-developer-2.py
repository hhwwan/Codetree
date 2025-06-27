ability = list(map(int, input().split()))

ability.sort()

team1 = ability[0] + ability[5]
team2 = ability[1] + ability[4]
team3 = ability[2] + ability[3]

answer = max(abs(team1 - team2), abs(team1 - team3), abs(team2 - team3))

print(answer)