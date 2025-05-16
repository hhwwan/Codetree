n, m = map(int, input().split())

def gcd(N,M):
    for i in range(min(N,M),0,-1): # 둘 중 더 작은 수 부터 역순으로
        if N % i == 0 and M % i == 0:
            return i

print(gcd(n,m))