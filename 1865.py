'''
웜홀은 도착했을 때의 시간이 출발했을 때 보다 뒤로 간다
음의 간선이 있다는 소린가?

음의 간선이 있으면 데이크스트라 못씀
플로이드 워셜이나 벨만 포드 써야하는데
느낌적으로 음의 간선이 있는 사이클이 생길 것 같다

조건 1. 출발점으로 돌아올 수 있는가? 출발점은 안주어졌으니 모든 노드가 출발점이 될 수 있다.
조건 2. 만약 출발점으로 돌아올 수 있다면 돌아왔을 때 시간이 처음보다 작아졌을까?

둘 다 가능하면 True 아니면 False
True는 한 번만 나와도 YES출력가능, 전부 False면 NO

음수 사이클이 존재한다, 그럼 음수 사이클에 포함되는 지점을 시작점이라고 생각하면 되잖아
그래서 여러 번 안돌리는 거네

입출력 확인 잘해...

'''

import sys
ssr = sys.stdin.readline

INF = 10001

def bellman_ford():
    min_time = [INF for _ in range(n+1)]
    min_time[1] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for next_node, next_time in routes[j]:
                if min_time[j]+next_time < min_time[next_node]:
                    min_time[next_node] = min_time[j]+next_time
                    if i == n:
                        return True
    return False

t = int(ssr())
for _ in range(t):
    n, m, w = map(int, ssr().split())
    routes = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, ssr().split())
        routes[s].append([e, t])
        routes[e].append([s, t])
    for _ in range(w):
        s, e, t = map(int, ssr().split())
        routes[s].append([e, -t])
    if bellman_ford():
        print('YES')
    else:
        print('NO')