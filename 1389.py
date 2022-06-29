from collections import deque
import sys
ssr = sys.stdin.readline

def sol(p):
    visited[p] = True
    q=deque([])
    q.append((p,0))
    b_num=0
    while q:
        a = q.popleft()
        b_num += a[1]
        for i in edges:
            if i[0] == a[0] and visited[i[1]] == False:
                q.append((i[1], a[1]+1))
                visited[i[1]] = True
            elif i[1] == a[0] and visited[i[0]] == False:
                q.append((i[0], a[1]+1))
                visited[i[0]] = True
    return b_num

n,m = map(int, ssr().split())
edges = [list(map(int, ssr().split())) for _ in range(m)]
idx = []
for i in range(1,n+1):
    visited = [False for _ in range(n+1)]
    idx.append(sol(i))
ans = idx.index(min(idx))+1
print(ans)