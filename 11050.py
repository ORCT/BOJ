import sys
ssr = sys.stdin.readline

def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

n,k = map(int, ssr().split())
print(int(fact(n)/(fact(k)*fact(n-k))))
#print(fact(n))
#print(fact(k))
#print(fact(n-k))