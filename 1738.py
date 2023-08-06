'''
단방향 간선

근데 최단이 아니라 최대한을 얻어야 하잖아
그럼 -INF로 초기화 하고 더 많은 양을 얻는 방향으로 움직이게 해야하나

근데 갔던 곳 또 가도 되는데 금품의 양이 최대가 되는 경로라고 하면
양의 사이클 하나 잡아서 죽어라 돌면 양의 무한대로 발산하는거 아닌가

최단 거리가 아니라 경로를 출력하는거네
이건 어떻게 하지

마지막에 한 번 더 돌면서 경로를 체크해야하나? 근데 그건 다른 노드로 갈 때 최댓값 받아서 가는 놈이 있을 수도 있잖아

이동이 가능하면 경로에 추가하면 되는데
한 노드에서 이동이 가능한 노드가 여러 개 있을 때는 뭘 경로에 넣을 것인가가 문제
예제 1이 좋은 예시인데
더 높아지기는 1 , 2, 3 순서로 가는게 좋은데
먼저 가는 놈을 집어넣으면 2가 들어가고
더 큰 가중치를 선택하면 3이 들어가
근데 실제로 구현해야 하는 것은 어떻게 경로를 돌더라도 최대한 큰 값을 만드는 거
어떻게 구현하면 2로 갔다가 3으로 가는게 최적의 경로라는 걸 집어넣을 수 있을까

동일한게 있다고 지우는 방식은 안됨 같은 노드 여러 번 방문이 가능해서

이동이 가능할 때 마다 노드 연결을 하는 배열을 따로 만들면?
유니온 파인드 처음 할 때 그거처럼

사이클이 있어도 최단거리로 도착할 수 있는 경우가 있음
그럼 사이클이 있어도 경로 재귀 탐색을 해야하는데
이 경우 처럼 최단 경로가 사이클에 안걸리면 상관없는데
사이클있어서 파인드했는데 사이클 걸려서 못빠져나가면, 그 땐 어떻게 이거 사이클이니까 -1해라고 할거야

재귀 몇 번 돌리다가 하지말라고 할거여? 근본적인 해결책이 아니지 않나
사이클에 출발점이나 도착점이 포함되는지를 체크하는 건 어때
가능하면 나쁘지 않은데 이거 어떻게 체크할거여?

사이클 노드도 체크했는데 이번엔 또 뭐여

시작 노드에 간선이 없는 경우가 있네

사이클에 포함은 되더라도 도달할 수 있으면 정답인가

양의 사이클이 존재해도 상관없이 도달할 수 있는 경우가 있고 도달할 수 없는 경우가 있음
사이클을 탔을 때 n번으로 갈 수 있는 경우와, n번으로 갈 수 없는 경우가 있음
사이클을 타도 n번으로 갈 수 있을 때는 최적의 경로가 아님, 죽을 때 까지 사이클타면 계속 값이 오르니까
사이클을 타면 n번으로 갈 수 없는 경우는 아예 사이클이 배제가 되기 때문에(애초에 사이클로 가면 도착을 못함) 최적의 경로도 도착가능

'''

import sys
ssr = sys.stdin.readline

INF = 987654321

def bellman_ford():
    for i in range(1, n+1):
        for cur_node, next_node, next_cost in edges:
            cost = max_cost[cur_node] + next_cost
            if max_cost[cur_node] != -INF and cost > max_cost[next_node]:
                max_cost[next_node] = cost
                routes[next_node] = cur_node
                if i == n:
                    max_cost[next_node] = INF
    
def find(node):
    if routes[node] != node:
        if max_cost[node] == INF:
            ans.append(-1)
            return
        else:
            find(routes[node])
    return ans.append(node)
                    
n, m = map(int, ssr().split())
edges = [list(map(int, ssr().split())) for _ in range(m)]
routes = [i for i in range(n+1)]
max_cost = [-INF for _ in range(n+1)]
max_cost[1] = 0
bellman_ford()
ans = []
find(n)
if -1 in ans:
    print(-1)
else:
    print(*ans)