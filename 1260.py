from collections import deque
import copy

def dfs(v):
    visited[v][v] = True
    print(v, end=' ')
    for i in range(1,n+1):
        if visited[v][i] == True and visited[i][i] == False:
            dfs(i)
        elif visited[i][v] == True and visited[i][i] == False:
            dfs(i)

def bfs():
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if visited1[v][i] == True and visited1[i][i] == False:
                q.append(i)
                visited1[i][i] = True
            elif visited1[i][v] == True and visited1[i][i] == False:
                q.append(i)
                visited1[i][i] = True

n,m,v = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(m)]
visited = [[False for _ in range(n+1)] for _ in range(n+1)]
for i in graph:
    visited[i[0]][i[1]] = True
visited1 = copy.deepcopy(visited)
q = deque([v])
visited1[v][v] = True
dfs(v)
print('')
bfs()
#스택으로 구현하면 추가 후 정렬을 한 번 하면 될 듯
#인접행렬로 구현하면 모든 경우를 대입하면서 찾으면 될듯
#지금 방법에서는 조건이 맞을 때 바로 재귀를 실행시켜버리니까 반복문 하나를 더 만들어서 조건문으로 해결 가능할 듯
