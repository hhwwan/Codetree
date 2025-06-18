a = input()

answer = int(a,2)
change = False

for i in range(1, len(a)):
    if a[i] == '0':
        answer += (2 ** (len(a) - 1 - i))
        change = True
        break

if not change:
    answer -= 1

print(answer)