a, b = map(int, input().split())
n = input()

tmp = 0
answer = []

for num in n:
    tmp = tmp * a + int(num)

while True:
    if tmp < b:
        answer.append(tmp)
        break
    answer.append(tmp % b)
    tmp //= b

for i in answer[::-1]:
    print(i, end='')