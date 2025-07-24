from collections import Counter

X, Y = map(int, input().split())

def interest_num(num):
    num_list = tuple(map(int, str(num)))

    if len(num_list) < 2:
        return 0

    counts = Counter(num_list)

    if len(counts) == 2:
        sort_value = sorted(counts.values())
        if sort_value[0] == 1 and sort_value[1] == len(num_list) - 1:
            return 1
    
    return 0

total = 0
for num in range(X, Y + 1):
    total += interest_num(num)

print(total)