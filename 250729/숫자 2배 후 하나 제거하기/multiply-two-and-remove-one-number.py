n = int(input())
arr = list(map(int, input().split()))

min_total = 10000
for i in range(n):
    for j in range(n):
        total = 0
        temp = arr[:]
        temp[i] *= 2 # 2배하기
        temp.pop(j) # 숫자 하나 제거

        for k in range(len(temp) - 1):
            total += (abs(temp[k] - temp[k+1]))
        
        min_total = min(min_total, total)

print(min_total)