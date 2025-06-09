N, B = map(int, input().split())
answer = []

while True:
    if N < B:
        answer.append(N)
        break
    answer.append(N % B)
    N //= B

for num in answer[::-1]:
    print(num, end='')