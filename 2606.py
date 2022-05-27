from collections import deque

n = int(input())
p = int(input())
graph =[list(map(int, input().split())) for _ in range(p)]
visited = [False for _ in range(n+1)]
q = deque()
visited[1]=True
q.append(1)
while q:
    v = q.popleft()
    #print(v)
    for i in range(p):
        if graph[i][0] == v:
            if visited[graph[i][1]] == False:
                q.append(graph[i][1])
                visited[graph[i][1]] = True
        elif graph[i][1] == v:
            if visited[graph[i][0]] == False:
                q.append(graph[i][0])
                visited[graph[i][0]] = True
            
print(sum(visited)-1)