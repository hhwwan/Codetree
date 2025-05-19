n = int(input())

def odd(a):
    if a % 2 == 0 and sum(map(int,str(a))) % 5 == 0:
        return 'Yes'
    else:
        return 'No'

print(odd(n)) 