a, b, c, d = map(int, input().split())

hour = (c - a) * 60
mins = d - b

print(hour+mins)