n = int(input())
S = input()

cnt = 0
for i in range(n): # C
    if S[i] == 'C':
        for j in range(i+1, n): # O
            if S[j] == 'O':
                for k in range(j+1, n): # W
                    if S[k] == 'W':
                        cnt += 1

print(cnt)