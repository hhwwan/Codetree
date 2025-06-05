n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

class Score:
    def __init__(self, name, korean, english, math):
        self.n = name
        self.k = korean
        self.e = english
        self.m = math

result = []

for i in range(n):
    result.append(Score(name[i], korean[i], english[i], math[i]))

result.sort(key=lambda x : (-x.k, -x.e, -x.m))

for j in range(n):
    print(result[j].n, result[j].k, result[j].e, result[j].m)