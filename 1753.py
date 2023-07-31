'''
가중치의 최대값이 10이라고 해서 가중치들의 합이 10보다 작다는 보장이 되는 것은 아니다.
간선의 갯수가 최대 30만개이고 가중치가 최대 10이므로 사실상 INF라는 상수를 초기화할 때는 10*30,000보다 큰 수를 넣어야 한다.
'''

import heapq
import sys
ssr = sys.stdin.readline

INF = 3000001

def dijkstra(start):
    h = [(0, start)]
    dist[start] = 0
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_dist > dist[cur_node]:
            continue
        for next_dist, next_node in routes[cur_node]:
            if dist[cur_node]+next_dist < dist[next_node]:
                dist[next_node] = dist[cur_node]+next_dist
                heapq.heappush(h, (dist[next_node], next_node))

v, e = map(int, ssr().split())
k = int(ssr())
routes = [[] for _ in range(v+1)]
dist = [INF for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, ssr().split())
    routes[a].append((c, b))
dijkstra(k)
for i in range(1, v+1):
    print(dist[i] if dist[i] != INF else 'INF')