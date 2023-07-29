'''
사이클이 만들어졌다면 만들어진 차례를, 아니라면 0을 출력

근데 어떻게 해야 유니온 파인드로 사이클을 구현하냐
3개 이상 연결되면 dfs를 따로 돌려서 사이클인지 확인을 할까

루트 노드가 같은데도 합치라는 명령이 나오면 그 때가 사이클이 완성된 시점 아닐까
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
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            uf[root1] = root2
        elif rank[root1] == rank[root2]:
            uf[root1] = root2
            rank[root2] += 1
        else:
            uf[root2] = root1
        return False
    else:
        return True
        
n, m = map(int, ssr().split())
uf = [i for i in range(n)]
rank = [0 for _ in range(n)]
for i in range(m):
    node1, node2 = map(int, ssr().split())
    result = union(node1, node2)
    if result:
        print(i+1)
        break
else:
    print(0)