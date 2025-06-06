m1, d1, m2, d2 = map(int, input().split())
A = input()

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day = 0

for i in range(m1, m2):
    day += num_of_days[i]

day += (d2 - d1)
target = day - day_of_the_week.index(A)

print(target // 7 + 1)  