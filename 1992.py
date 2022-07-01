import sys
ssr = sys.stdin.readline

def sol(r,c,l):
    global ans
    check = t[r][c]
    for i in range(r,r+l):
        for j in range(c,c+l):
            if t[i][j] != check:
                ans += '('
                sol(r,c,l//2)
                sol(r,c+l//2,l//2)
                sol(r+l//2,c,l//2)
                sol(r+l//2,c+l//2,l//2)
                ans += ')'
                return
    ans += check
    
n = int(ssr())
t = [list(ssr().rstrip()) for _ in range(n)]
ans=''
sol(0,0,n)
print(ans)