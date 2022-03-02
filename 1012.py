import sys
sys.setrecursionlimit(10**6)
ssr = sys.stdin.readline

def sol(x,y):
    if x<0 or x>=m or y<0 or y>=n:
        return
    if farm[x][y] == 0:
        return
    farm[x][y]=0
    sol(x-1,y)
    sol(x+1,y)
    sol(x,y-1)
    sol(x,y+1)

t = int(ssr())
for _ in range(t):
    m,n,k = map(int,ssr().split())
    farm = [[0 for _ in range(n)] for _ in range(m)]
    bug=0
    for _ in range(k):
        x,y = map(int, ssr().split())
        farm[x][y] = 1
    for i in range(m):
        for j in range(n):
            if farm[i][j] == 1:
                sol(i,j)
                bug += 1
    print(bug)