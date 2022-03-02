import sys
ssr = sys.stdin.readline

def sol(n,r,c):
    global result
    if n==0:
        return
    if r<2**(n-1) and c<2**(n-1):
        sol(n-1,r,c)
    elif r<2**(n-1) and c>=2**(n-1):
        result += (2**(n-1))*(2**(n-1))
        sol(n-1,r,c-2**(n-1))
    elif r>=2**(n-1) and c<2**(n-1):
        result += 2*((2**(n-1))*(2**(n-1)))
        sol(n-1,r-2**(n-1),c)
    else:
        result += 3*((2**(n-1))*(2**(n-1)))
        sol(n-1,r-2**(n-1),c-2**(n-1))
    return
    
n,r,c = map(int, ssr().split())
result = 0
sol(n,r,c)
print(result)