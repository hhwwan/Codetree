def no_carry(a,b,c):
    sa = str(a)[::-1]
    sb = str(b)[::-1]
    sc = str(c)[::-1]

    max_len = max(len(sa), len(sb), len(sc))

    for i in range(max_len):
        da = int(sa[i]) if i < len(sa) else 0
        db = int(sb[i]) if i < len(sb) else 0
        dc = int(sc[i]) if i < len(sc) else 0

        if da + db + dc >= 10:
            return False
    return True

n = int(input())
arr = [int(input()) for _ in range(n)]

max_total = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if no_carry(arr[i], arr[j], arr[k]):
                total = arr[i] + arr[j] + arr[k]
                if total > max_total:
                    max_total = total

print(max_total)