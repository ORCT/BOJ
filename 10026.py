from collections import deque
import sys
ssr = sys.stdin.readline

def sol():
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                q.append((i,j))
                visited[i][j] = 1
                c = t[i][j]
                while q:
                    tmp = q.popleft()
                    for k in dp:
                        if 0 <= tmp[0]+k[0] < n and 0 <= tmp[1]+k[1] < n:
                            if visited[tmp[0]+k[0]][tmp[1]+k[1]] == 0:
                                if t[tmp[0]+k[0]][tmp[1]+k[1]] == c:
                                    q.append((tmp[0]+k[0], tmp[1]+k[1]))
                                    visited[tmp[0]+k[0]][tmp[1]+k[1]] = 1
                ans[0] += 1
            else:
                continue
                                              
def sol1():
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                q.append((i,j))
                visited[i][j] = 0
                c = t[i][j]
                while q:
                    tmp = q.popleft()
                    for k in dp:
                        if 0 <= tmp[0]+k[0] < n and 0 <= tmp[1]+k[1] < n:
                            if visited[tmp[0]+k[0]][tmp[1]+k[1]] == 1:
                                if c == 'R' or c == 'G':
                                    if t[tmp[0]+k[0]][tmp[1]+k[1]] == 'B':
                                        continue
                                    else:
                                        q.append((tmp[0]+k[0], tmp[1]+k[1]))
                                        visited[tmp[0]+k[0]][tmp[1]+k[1]] = 0
                                else:
                                    if t[tmp[0]+k[0]][tmp[1]+k[1]] == c:
                                        q.append((tmp[0]+k[0], tmp[1]+k[1]))
                                        visited[tmp[0]+k[0]][tmp[1]+k[1]] = 0
                ans[1] += 1
            else:
                continue
            
n = int(ssr())
t = [list(ssr()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
q = deque([])
dp = [(-1,0),(1,0),(0,-1),(0,1)]
ans=[0,0]
sol()
sol1()
print(*ans)                