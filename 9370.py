'''
입력이 많아서 귀찮다

교차로의 갯수 = 노드의 갯수
교차로 사이에는 도로가 많아봐야 1개다 = 같은 지점을 연결하는 간선은 최대 1개만 존재한다.
교차로라는 말 보다는 분기점이나 교차점이라고 표현하는게 더 명료했을 것 같아 아쉽다.

출발지점과 무조건 거치는 경로가 주어짐
g와 h 사이의 양방향 도로는 최단 경로에 무조건 포함한다.

목적지 후보간의 최단거리 길이를 비교할 필요는 없고
그냥 최단거리로 구한 경로 안에 필수 루트가 포함이 되기만 하면 되는 듯?

최단거리의 경로가 여러 개 존재할 수 있음 = 어차피 값으로 비교하는데 나는 신경 안써도 되는거 아닌가


'''

import heapq
import sys
ssr = sys.stdin.readline

INF = 2000001

def dijkstra(start, end=None):
    h = [(0, start)]
    min_dist = [INF for _ in range(n+1)]
    min_dist[start] = 0
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_dist > min_dist[cur_node]:
            continue
        for next_dist, next_node in routes[cur_node]:
            dist = min_dist[cur_node] + next_dist
            if dist < min_dist[next_node]:
                min_dist[next_node] = dist
                heapq.heappush(h, (min_dist[next_node], next_node))
    if end == None:
        return min_dist
    else:
        return min_dist[end]

c = int(ssr())
for _ in range(c):
    n, m, t = map(int, ssr().split())
    s, g, h = map(int, ssr().split())
    routes = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, ssr().split())
        if (a == h and b == g) or (a == g and b == h):
            d -= 0.1
        routes[a].append((d, b))
        routes[b].append((d, a))
    distance = dijkstra(s)
    ans = []
    for _ in range(t):
        x = int(ssr())
        if type(distance[x]) != int:
            ans.append(x)
    print(*sorted(ans))