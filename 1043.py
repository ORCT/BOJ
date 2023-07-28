'''
지민이가 거짓말쟁이가 되지 않는 방법
지민이는 모든 파티에 참여해야한다.
진실을 아는 사람 앞에서는 사실만 말해야한다

이미 진실을 들은 사람에게는 진실만을
이미 거짓을 들은 사람에게는 거짓만을

즉 진실을 아는 사람과 한 번이라도 같은 파티에 참석하는 사람들에게는 거짓을 말할 수 없다

knowing_truth에 값을 추가하고 다 체크하려고 했는데 그냥 사람 번호만큼 배열 만들고
그 값이 1이면 진실을 아는 사람, 0이면 모르는 사람해서 인덱스로 호출해보면 O(1)로 체크 가능하지 않나

지민이가 사람들의 스케줄을 전부 체크한 후에 거짓말을 할 수 있겠다는 생각이 드는 파티의 수를 결과로 출력한다.
미리 체크가 가능해야한다
하면서 체크할 경우 사실은 거짓말을 하면 안되는 파티가 포함이 안될 수 있다

반례:
5 4
1 5
2 1 2
2 2 3
2 3 4
2 4 5
>> 0

순서대로만 집어넣는 건 약간 위험하겠다.
진실을 표기할 때 마다 반복문을 돌도록 해야하나
파티 목록도 방문처리를 하면 이미 체크한 목록은 안돌아도 되려나?(어차피 사람을 진실 표시를 하면 자동으로 이미 체크한 파티는 안돌듯)

bfs처럼 해서 queue 안에 있는 인자를 빼가지고 파티 목록을 돌도록 하면?

분리 집합에 대해서 알아보자
분리 집합(disjoint set)이란?
분리 집합은 서로소 집합이라고도 한다. (서로소란 대수 관계에서는 1 이외의 공약수가 없는 것을 의미하지만 집합에서는 공통 원소가 없는 집합을 말한다)

유니온파인드(Union-Find) : (트리)합치기&(root)찾기
유니온 파인드 알고리즘은 그래프 탐색 알고리즘 중 하나로, 같은 연결요소인지 반대로 다른 연결요소인지를 찾을 수 있는 알고리즘이다.
각 그룹을 트리의 형태로 표현한다
각 노드마다 그 노드의 부모 노드 번호를 기록하여 트리 구조로 나타낸다
이렇게 나타낸 트리는 root 노드를 갖는데, 이 root 노드를 통해 그룹을 구별할 수 있게 된다(root노드는 자기 자신을 기록하면 됨).

유니온 파인드의 장점이 뭐야?
그래프 탐색을 할 때 새로운 간선이 생길 때 마다 bfs/dfs처럼 완전 탐색(최악의 경우 완전탐색(그냥 완전 탐색은 브루트포스다)이지 정확하게는)을 진행하지 않고 같은 그룹인지 확인 가능
지금 풀고 있는 문제에서 연결요소 체크할 때도 도움되지 않을까?
이건 분명 사용처가 무궁무진하다.
확실한 건 반복해서 그룹확인을 해야할 경우에 연산량을 많이 줄여줄 것

Find의 시간복잡도가 트리의 높이(깊이)에 의해 결정되므로
새로운 노드를 연결할 때 연결하는 노드의 부모 노드를 root 노드로 만들어 준다면(root에 바로 붙인다면) 보다 효율적일 것이다.
이 최적화 방법을 경로 압축(path compression)이라고 한다.

그래서 최적화 방법으로 union by rank가 있다
높이가 낮은 트리를 높은 트리에 붙여서 시간 복잡도를 줄일 수 있다.
높은 트리를 낮은 트리에 붙이는 경우 합친 이후의 트리의 높이가 높은 트리와 같거나 1만큼 늘어날 수 있음
반대로 낮은 트리를 높은 트리에 붙이면 전체 트리의 높이가 변하지 않기 때문에 시간복잡도가 증가하지 않는다.
따라서 낮은 쪽을 높은 쪽에 붙이는 것이 더 효율적이다.

그러면 이제 이 문제에 유니온 파인드를 한 번 적용해볼까?
'''

'''from collections import deque
import sys
ssr = sys.stdin.readline

def check_truth():
    while q:
        p = q.popleft()
        for party in parties:
            if p in party[1:]:
                for i in party[1:]:
                    if visited[i] == False:
                        q.append(i)
                        visited[i] = True
    
n, m = map(int, ssr().split())
knowing_truth = list(map(int, ssr().split())) # 0 : num of person, 1~ : person's num
visited = [False for _ in range(n+1)]
q = deque([])
for i in knowing_truth[1:]:
    visited[i] = 1
    q.append(i)
parties = [list(map(int, ssr().split())) for _ in range(m)]
check_truth()
for party in parties:
    for i in party[1:]:
        if visited[i] == 1:
            m -= 1
            break
print(m)'''

# Union-Find
import sys
ssr = sys.stdin.readline

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
    
def find(node):
    if uf[node] == node:
        return node
    else:
        uf[node] = find(uf[node])
        return uf[node]

n, m = map(int, ssr().split())
knowing_truth = list(map(int, ssr().split()))
parties = [list(map(int, ssr().split())) for _ in range(m)]
uf = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]
if knowing_truth[0] != 0:
    for i in knowing_truth[1:]:
        uf[i] = knowing_truth[1]
    rank[knowing_truth[1]] = 1
cnt = 0
for people in parties:
    for i in people[1:]:
        union(people[1], i)
for people in parties:
    if knowing_truth[0] != 0:
        if uf[find(knowing_truth[1])] == uf[find(people[1])]:
            cnt += 1
print(m-cnt)