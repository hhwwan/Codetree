a, b = map(int, input().split())

def game(A):
    if '3' in str(A) or '6' in str(A) or '9' in str(A):
        return 1

def multiple(B):
    if B % 3 == 0:
        return 1

cnt = 0
for i in range(a,b+1):
    if game(i) or multiple(i):
        cnt += 1

print(cnt)