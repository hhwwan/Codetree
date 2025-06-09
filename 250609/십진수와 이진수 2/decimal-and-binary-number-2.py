N = input()
tmp = 0
answer = []

for num in N:
    tmp = tmp * 2 + int(num)

tmp *= 17

while True:
    if tmp < 2:
        answer.append(tmp)
        break
    answer.append(tmp % 2)
    tmp //= 2

for i in answer[::-1]:
    print(i, end='')