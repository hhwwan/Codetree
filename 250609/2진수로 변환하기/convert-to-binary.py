n = int(input())
answer = ''

while True:
    if n == 1:
        answer += '1'
        break
    else:
        answer += str(n % 2)
        n //= 2

print(answer[::-1])