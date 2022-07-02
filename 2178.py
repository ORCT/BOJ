from collections import deque
import sys
ssr = sys.stdin.readline

def sol():
    while q:
        r,c,s = q.popleft()
        if r == n-1 and c == m-1:
            return s
        for i in range(4):
            if r+dr[i] < 0 or r+dr[i] >= n or c+dc[i] <0 or c+dc[i] >= m:
                continue
            else:
                if t[r+dr[i]][c+dc[i]] == '1' and visited[r+dr[i]][c+dc[i]] == False:
                    q.append((r+dr[i],c+dc[i],s+1))
                    visited[r+dr[i]][c+dc[i]] = True
        
n,m = map(int, ssr().split())
t = [list(ssr().rstrip()) for _ in range(n)]
q = deque([(0,0,1)])
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True
dr = [-1,1,0,0]
dc = [0,0,-1,1]
ans = sol()
print(ans)