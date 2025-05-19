n = int(input())

def divide(a):
    total = 0
    for i in range(1,a+1):
        total += i
    return total // 10

print(divide(n))