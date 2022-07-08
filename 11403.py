'''from collections import deque
import sys
ssr = sys.stdin.readline

n = int(ssr())
g = [list(map(int, ssr().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
q = deque([(0,0,0)])
visited[0][0] = 1
while q:
    r,c,s = q.popleft()
    for i in range(n):
        if g[c][i] == 1:
            if visited[c][i] == 0 or visited[s][i]==0:
                q.append((c,i,c))
                q.append((c,i,s))
                visited[c][i]=1
                visited[s][i]=1
for i in visited:            
    print(*i)'''
    
import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(10000)

def sol(r,c,start):
    if visited[r][c] == 1:
        g[start][c] = 1
        g[r][c] = 1 
        return
    visited[r][c] = 1
    visited[c][r] = 1
    g[start][c] = 1
    g[r][c] = 1
    for i in range(n):
        if g[c][i] == 1:
            sol(c,i,start)

n = int(ssr())
g = [list(map(int, ssr().split())) for _ in range(n)]
for i in range(n):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        if g[i][j] == 1:
            sol(i,j,i)
for i in g:            
    print(*i)

