import sys
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
print(cnt)