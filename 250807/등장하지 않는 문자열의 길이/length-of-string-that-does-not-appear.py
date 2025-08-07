N = int(input())
str = input()

for length in range(1, N + 1):
    substrings = set()
    found = False
    for j in range(N - length + 1):
        word = str[j:j+length]
        # word가 string안에 있다면 pass
        if word in substrings:
            found = True
            break
        # word안에 없다면 string에 추가
        substrings.add(word)
    if not found:
        print(length)
        break