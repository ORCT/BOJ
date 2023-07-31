'''
1번에서 N번으로 이동하는데 무조건 통과해야하는 정점 2개가 주어짐
즉 데이크스트라를 3번 사용하면 될 것으로 보인다
1번에서 v1번, v1번에서 v2번, v2번에서 N번

굳이 1에서 v1으로 가고 v1 에서 v2로 v2에서 n으로 가는 순서를 지킬 필요는 없다
1에서 n으로 가는 동안에 v1과 v2를 거치기만 하면 됨

방문하는 노드를 다 기록해뒀다가 통과를 안하면 다시 통과를 하게 해야하나(다시했을 때 이게 최단거리란 보장이 있나)
'''

import heapq
import sys
ssr = sys.stdin.readline

INF = 200000001

def dijkstra(start, end):
    h = [(0, start)]
    min_dist = [INF for _ in range(n+1)]
    min_dist[start] = 0
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_dist > min_dist[cur_node]:
            continue
        for next_dist, next_node in edges[cur_node]:
            if min_dist[cur_node]+next_dist < min_dist[next_node]:
                min_dist[next_node] = min_dist[cur_node]+next_dist
                heapq.heappush(h, (min_dist[next_node], next_node))
    return min_dist[end]
        
def sol(v1, v2):
    ans = min(dijkstra(1, v1)+dijkstra(v1, v2)+dijkstra(v2, n), dijkstra(1, v2)+dijkstra(v2, v1)+dijkstra(v1, n))
    print(ans if ans< INF else -1)
    
n, e = map(int, ssr().split())
edges = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, ssr().split())
    edges[a].append((c, b))
    edges[b].append((c, a))
v1, v2 = map(int, ssr().split())
sol(v1, v2)