a = input()

answer = int(a,2)

for i in range(1, len(a) + 1):
    if a[i] == '0':
        answer += (2 ** (len(a) - i - 1))
        break

print(answer)