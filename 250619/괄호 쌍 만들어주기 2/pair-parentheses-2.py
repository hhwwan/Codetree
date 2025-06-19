A = input()

cnt = 0
for i in range(1, len(A)):
    if A[i] == '(' and A[i-1] == '(':
        for j in range(i+1, len(A)):
            if A[j] == ')' and A[j-1] == ')':
                cnt += 1

print(cnt)