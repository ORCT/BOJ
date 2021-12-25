import sys
ssr = sys.stdin.readline

def gcd(n,m):
    if n%m == 0:
        return m
    else:
        return gcd(m,n%m)

a,b = map(int, ssr().split())
if a<b: a,b=b,a
g = gcd(a,b)
print(g)
print(int(a*b/g))