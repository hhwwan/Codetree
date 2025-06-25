n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(str(num))
    b.append(cnt1)
    c.append(cnt2)

answer = 0

for i in range(123, 987):
    number = str(i)

    # 0이 안들어가있고, 숫자 중복 x
    if '0' in number or len(set(number)) < 3:
        continue
    
    flag = True
    for j in range(n):
        s = 0
        ba = 0
        for k in range(3):
            if number[k] == a[j][k]:
                s += 1
            elif number[k] in a[j]:
                ba += 1
        
        if s != b[j] or ba != c[j]:
            flag = False
            break
    
    if flag:
        answer += 1

print(answer)