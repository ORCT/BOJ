'''
union find 연습문제
'''

import sys
ssr = sys.stdin.readline
sys.setrecursionlimit(1000000)

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            uf[root1] = root2
        elif rank[root1] == rank[root2]:
            uf[root1] = root2
            rank[root1] += 1
        else:
            uf[root2] = root1
    return

def find(node):
    if uf[node] == node:
        return node
    else:
        uf[node] = find(uf[node])
        return uf[node]
    
n, m = map(int, ssr().split())
uf = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]
for _ in range(m):
    query, node1, node2 = map(int, ssr().split())
    if query == 0:
        union(node1, node2)
    else:
        if find(node1) == find(node2):
            print('yes')
        else:
            print('no')