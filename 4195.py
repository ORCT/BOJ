'''
숫자가 아니니까 딕셔너리로 연결하면 될듯?

어떻게 하면 친구의 숫자를...
유니온 하면서 친구수를 더해서 저장할까
'''

from collections import defaultdict
import sys
ssr = sys.stdin.readline

def find(name):
    if uf[name] == name:
        return name
    else:
        uf[name] = find(uf[name])
        return uf[name]
    
def union(name1, name2):
    root1 = find(name1)
    root2 = find(name2)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            uf[root1] = root2
            rank[root2] += rank[root1]
        elif rank[root1] == rank[root2]:
            uf[root1] = root2
            rank[root2] += rank[root1]
        else:
            uf[root2] = root1
            rank[root1] += rank[root2]
            
t = int(ssr())
for _ in range(t):
    uf = {}
    rank = defaultdict(lambda:1)
    f = int(ssr())
    for _ in range(f):
        people = ssr().rstrip().split()
        for i in people:
            if not i in uf.keys():
                uf[i] = i
        union(people[0], people[1])
        print(rank[find(people[1])])