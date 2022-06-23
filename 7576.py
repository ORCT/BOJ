import sys
from collections import deque
ssr = sys.stdin.readline

def sol(r,c,day):
    if visited[r][c] == True:
        return
    visited[r][c] = True
    for i in range(4):
        if 0<=r+dr[i]<m and 0<=c+dc[i]<n and visited[r+dr[i]][c+dc[i]] == False and t[r+dr[i]][c+dc[i]] == 0:
            q.append((r+dr[i],c+dc[i],day+1))
            t[r+dr[i]][c+dc[i]] = 1
            
dr = [-1,1,0,0]
dc = [0,0,-1,1]    
n,m = map(int, ssr().split())
t = [list(map(int, ssr().split())) for _ in range(m)]
q = deque([])
visited = [[False for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        if t[i][j] == 1:
            q.append((i,j,0))
ans = 0
while q:
    qr,qc,day = q.popleft()
    sol(qr,qc,day)
    ans = day
for i in range(m):
    for j in range(n):
        if t[i][j] == 0:
            ans = -1
            break
print(ans)