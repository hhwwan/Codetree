n = int(input())

def number(N):
    num = 1
    for i in range(N):
        for j in range(N):
            print(num, end=' ')
            num += 1
            if num > 9:
                num = 1
        print() # N개 출력 후 줄 바꿈

number(n)