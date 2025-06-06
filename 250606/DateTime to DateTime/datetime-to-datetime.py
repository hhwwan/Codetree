a, b, c = map(int, input().split())

day = (a-11) * 1440
hour = (b-11) * 60
mins = c - 11

result = day + hour + mins

if result < 0:
    print(-1)
else:
    print(result)