n, m = map(int, input().split())

# 최소공약수 구하기
def gcd(N,M):
    for i in range(min(N,M),0,-1):
        if N % i == 0 and M % i == 0:
            return i

# 최소공약수를 이용하여 최대공배수 구하기
def lcm(N,M):
    return (N * M) // gcd(N,M)

print(lcm(n,m))