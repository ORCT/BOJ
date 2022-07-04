from collections import deque
import sys
ssr = sys.stdin.readline

def sol():
    global num
    while q:
        r,c = q.popleft()
        for i in range(4):
            if 0<=r+dr[i]<n and 0<=c+dc[i]<n:
                if t[r+dr[i]][c+dc[i]] == '1' and visited[r+dr[i]][c+dc[i]] == False:
                    num += 1
                    q.append((r+dr[i],c+dc[i]))
                    visited[r+dr[i]][c+dc[i]] = True

n = int(ssr())
t = [list(ssr().rstrip()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
q = deque([])
dr = [-1,1,0,0]
dc = [0,0,-1,1]
ans = []
for i in range(n):
    for j in range(n):
        if t[i][j] == '1' and visited[i][j] == False:
            q.append((i,j))
            visited[i][j] = True
            num = 1
            sol()
            ans.append(num)
print(len(ans))
ans.sort()
for i in ans:
    print(i)