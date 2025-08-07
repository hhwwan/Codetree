N = int(input())
str = input()

answer = 101
for i in range(1, N):
    word = str[0:i]
    found = False
    for j in range(i, N - 1):
        if j + i <= N:
            if word == str[j:j+i]:
                found = True
                break
    if not found:
        answer = min(answer, len(word))
print(answer)