a, b, c = map(int, input().split())

day, hour, mins = 11, 11, 11
elapsed_mins = 0

while True:
    if day == a and hour == b and mins == c:
        break

    elapsed_mins += 1
    mins += 1

    if mins > 60:
        hour += 1
        mins = 1
    
    if hour > 23:
        day += 1
        hour = 0

print(elapsed_mins)
