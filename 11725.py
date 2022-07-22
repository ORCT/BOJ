from collections import deque
import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(parent):
    if visited[parent] == 1:
        return
    visited[parent] = 1
    for i in adjacency_list[parent]:#edge를 다 돌기 때문에 시간초과가 나오는 것
        if visited[i] == 0:
            ans[i] = parent
            dfs(i)

def bfs():
    q = deque([])
    for i in adjacency_list[1]:
        ans[i] = 1
        q.append(i)
        visited[i] = 1
    while q:
        tmp = q.popleft()
        for i in adjacency_list[tmp]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                ans[i] = tmp

n = int(input())
adjacency_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, ssr().split())
    adjacency_list[a].append(b)
    adjacency_list[b].append(a)
visited = [0 for _ in range(n+1)]
ans=[0 for _ in range(n+1)]
# dfs(1)
bfs()
for i in range(2,n+1):
    print(ans[i])
    
'''
일단 한 번만 적힌 놈은 무조건 자식이다
즉 그 자식하고 연결된 놈은 그 놈의 부모지
dfs나bfs를 쓰면 어떤 순서로 탐색하는지 알 수 있잖아
그럼 탐색할 때 어디서 어디로 이어지는지 알 수 있다는 뜻이니까
그게 부모 자식 관계를 표현하는 것이라고 할 수 있지않나?
n이 10만이니까 n^2은 못쓰겠네
어차피 트리는 root로 부터 모조리 갈 수 있으므로 굳이 반복문을 만들 필요는 없지

인접 리스트를 이용해서 연결되어 있는 놈들만 골라놓은 배열에서 dfs를 쓰면 훨씬 간단할 것
'''