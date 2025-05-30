n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

class Region:
    def __init__(self, name, address, region):
        self.n = name
        self.a = address
        self.r = region

result = []
for i in range(n):
    result.append(Region(name[i], street_address[i], region[i]))

sort_result = sorted(result, key = lambda x : x.n, reverse=True)
print('name', sort_result[0].n)
print('addr', sort_result[0].a)
print('city', sort_result[0].r)