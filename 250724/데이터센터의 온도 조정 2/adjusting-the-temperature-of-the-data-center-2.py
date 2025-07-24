N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]
max_ranges = max(ranges, key = lambda x : x[1])

def tool_A(temp):
    total = 0
    for T in range(N):
        if temp < ranges[T][0]:
            total += C
        elif temp >= ranges[T][0] and temp <= ranges[T][1]:
            total += G
        elif temp > ranges[T][1]:
            total += H
    return total

max_tool = 0
for temp in range(1, max_ranges[1] + 2):
    max_tool = max(max_tool, tool_A(temp))

print(max_tool)