abilities = list(map(int, input().split()))

def team(a, b, c):
    sum1 = a + b + c
    sum2 = sum(abilities) - sum1
    return abs(sum1 - sum2)

min_value = 1000000

for i in range(len(abilities)):
    for j in range(i+1, len(abilities)):
        for k in range(j+1, len(abilities)):
            min_value = min(team(abilities[i], abilities[j], abilities[k]), min_value)

print(min_value)