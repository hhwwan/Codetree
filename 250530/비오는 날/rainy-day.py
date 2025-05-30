n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

result = []
for i in range(n):
    result.append(Data(date[i], day[i], weather[i]))

rain_days = [item for item in result if item.weather == 'Rain']

if rain_days:
    early = rain_days[0]
    for i in rain_days[1:]:
        if i.date < early.date:
            early = i
    
    print(early.date, early.day, early.weather)