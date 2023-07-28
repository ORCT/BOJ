'''
다른 도시를 경유해도 괜찮으니까 해당 여행 경로가 가능한지 체크

root 노드가 동일하면 어떻게든지 갈 수 있다는 뜻 아님?
양방향성이라고 가정하면 다른 가지여도 root 타고 가면 그만 아냐

근데 유니온 파인드가 아니라 bfs인 쪽이 좀 더 빠를 거 같다는 생각은 든다
'''

import sys
ssr = sys.stdin.readline

def find(node):
    if uf[node] == node:
        return node
    else:
        uf[node] = find(uf[node])
        return uf[node]
    
def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            uf[root1] = root2
        elif rank[root1] == rank[root2]:
            uf[root1] = root2
            rank[root2] += 1
        else:
            uf[root2] = root1

n = int(ssr())
m = int(ssr())
uf = [i for i in range(n)]
rank = [0 for _ in range(n)]
for i in range(n):
    line = list(map(int, ssr().split()))
    for j in range(n):
        if line[j] == 1:
            union(i, j)
route = list(map(lambda x : int(x)-1, ssr().split()))
check = uf[find(route[0])]
for i in range(1, len(route)):
    if check != uf[find(route[i])]:
        print('NO')
        break
else:
    print('YES')