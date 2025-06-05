n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

class Info:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

result = []

for i in range(5):
    result.append(Info(name[i], height[i], weight[i]))

result.sort(key=lambda x : x.n)

print("name")
for j in range(5):
    print(result[j].n, result[j].h, result[j].w)
print()

result.sort(key=lambda x : -x.h)

print("height")
for j in range(5):
    print(result[j].n, result[j].h, result[j].w)