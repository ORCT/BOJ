from collections import deque
import sys
ssr = sys.stdin.readline

m,n,h = map(int, ssr().split())
t = [[list(map(int, ssr().split())) for _ in range(n)] for _ in range(h)]
q = deque([])
dp=[(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]#h,n,m
for i in range(h):
    for j in range(n):
        for k in range(m):
            if t[i][j][k] == 1:
                q.append((i,j,k,0))
ans = 0
while q:
    tmp = q.popleft()
    for i in dp:
        if 0 <= tmp[0]+i[0] < h and 0 <= tmp[1]+i[1] < n and 0 <= tmp[2]+i[2] < m:
            if t[tmp[0]+i[0]][tmp[1]+i[1]][tmp[2]+i[2]] == 0:
                q.append((tmp[0]+i[0],tmp[1]+i[1],tmp[2]+i[2],tmp[3]+1))
                t[tmp[0]+i[0]][tmp[1]+i[1]][tmp[2]+i[2]] = 1
    ans = tmp[3]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if t[i][j][k] == 0:
                ans = -1
                break
print(ans)