'''import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def sol(v):
    if visited[v] == True:
        return
    else:
        visited[v] = True
        for i in range(len(edges)):
            if edges[i][0] == v:
                sol(edges[i][1])
            elif edges[i][1] == v:
                sol(edges[i][0])
        return v
    
n,m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
visited = [False for _ in range(n+1)]
cnt = 0
for i in range(1,n+1):
    a = sol(i)
    if i == a:
        cnt += 1
print(cnt)'''

from collections import deque
import sys
ssr = sys.stdin.readline

n, m = map(int, ssr().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, ssr().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(n+1)]
q = deque([])
ans = 0
for i in range(1, n+1):
    if visited[i] == False:
        visited[i] = True
        q.append(i)
        ans += 1
        while q:
            now = q.popleft()
            for j in graph[now]:
                if visited[j] == False:
                    q.append(j)
                    visited[j] = True
print(ans)