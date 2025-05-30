MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class code:
    def __init__(self, codename, score):
        self.c = codename
        self.s = score

result = []
for i in range(MAX_N):
    result.append(code(codenames[i], scores[i]))

min_score = result[0]
for score in result[1:]:
    if score.s < min_score.s:
        mis_score = score

print(min_score.c, min_score.s)