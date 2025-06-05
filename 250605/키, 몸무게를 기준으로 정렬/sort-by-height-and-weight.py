n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

class Info:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

result = []

for i in range(n):
    result.append(Info(name[i], height[i], weight[i]))

result.sort(key=lambda x : (x.h, -x.w))

for j in range(n):
    print(result[j].n, result[j].h, result[j].w)