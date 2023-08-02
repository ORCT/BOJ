'''
단방향 그래프
갔다가 와야함
최단시간
데이크스트라
제일 시간 오래걸리는 사람 출력

제일 시간이 많이 걸린 사람이 여러명인 경우는 없는건가

원래 그래프를 사용해서 각 노드에서 x로 출발하는데 걸리는 최단거리가
간선 정보를 뒤집어서 x에서 각 노드로 가는거랑 같음
그래서 뒤집어서 사용
'''

import heapq
import sys
ssr = sys.stdin.readline

INF = 1000001

def dijkstra(start, edges):
    time = [INF for _ in range(n+1)]
    time[start] = 0
    h = [(0, start)]
    while h:
        cur_time, cur_node = heapq.heappop(h)
        if cur_time > time[cur_node]:
            continue
        for next_time, next_node in edges[cur_node]:
            cost = time[cur_node] + next_time
            if cost < time[next_node]:
                time[next_node] = cost
                heapq.heappush(h, (time[next_node], next_node))
    return time

n, m, x = map(int, ssr().split())
routes = [[] for _ in range(n+1)]
reverse_routes = [[] for _ in range(n+1)]
for _ in range(m):
    departure, arrival, time = map(int, ssr().split())
    routes[departure].append((time, arrival))
    reverse_routes[arrival].append((time, departure))
time_take = [0 for _ in range(n+1)]
time_take = dijkstra(x, routes)
reversed_time_take = dijkstra(x, reverse_routes)
max_time = 0
for i in range(1, n+1):
    max_time = max(max_time, time_take[i]+reversed_time_take[i])
print(max_time)