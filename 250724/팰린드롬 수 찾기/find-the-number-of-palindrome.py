X, Y = map(int, input().split())

cnt = 0
for num in range(X, Y + 1):
    list_num = list(map(int, str(num)))
    reverse_num = list_num[::-1]
    if list_num == reverse_num:
        cnt += 1
print(cnt)