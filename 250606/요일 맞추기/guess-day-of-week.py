m1, d1, m2, d2 = map(int, input().split())

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def jan1(month, day):
    total_days = 0
    for i in range(1, month):
        total_days += num_of_days[i]
    total_days += day

    return total_days

start_day = jan1(m1, d1)
end_day = jan1(m2, d2)

result = end_day - start_day

print(day_of_the_week[result % 7])