n = int(input())
answer = []

while True:
    if n == 1:
        answer.append(1)
        break
    answer.append(n % 2)
    n //= 2

for i in answer[::-1]:
    print(i, end='')