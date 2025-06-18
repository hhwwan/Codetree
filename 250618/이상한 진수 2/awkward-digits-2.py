a = input()

answer = int(a,2)

for i in range(1, len(a)):
    if a[i] == '0':
        answer += (2 ** (len(a) - 1 - i))
        break

print(answer)