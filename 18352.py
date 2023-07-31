'''
모든 도로의 길이가 1이기 때문에 데이크스트라를 쓰지 않아도 풀 수 있다
하지만 데이크스트라로 풀어보자

데이크스트라의 과정
1. 시작 노드를 정한다.
2. 시작노드부터 각 노드까지의 최단거리 배열을 초기화한다.
3. 가장 가까운 노드부터 방문하면서 배열을 갱신한다.

3의 과정
3-1. 우선순위큐를 초기화한다.
3-2. 아직 방문하지 않은 노드 중에서 가장 가까운 노드를 (현재 이동 거리 + 노드까지의 거리, 노드)를 원소로 우선순위큐에 넣는다.
3-3. 원소를 pop해서 3-2를 반복
'''

import heapq
import sys
ssr = sys.stdin.readline

INF = 300001

def dijkstra():
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_dist > dist[cur_node]:
            continue
        for next_dist, next_node in routes[cur_node]:
            if dist[cur_node]+next_dist < dist[next_node]:
                dist[next_node] = dist[cur_node] + next_dist
                heapq.heappush(h, (dist[next_node], next_node))
        
n, m, k, x = map(int, ssr().split())
routes = [[] for _ in range(n+1)]
for _ in range(m):
    departure, arrival = map(int, ssr().split())
    routes[departure].append((1, arrival))
dist = [INF for _ in range(n+1)]
h = [(0, x)]
dist[x] = 0
dijkstra()
ans = []
for i in range(1, n+1):
    if dist[i] == k:
        ans.append(i)
if len(ans) != 0:
    print(*ans, end='\n')
else:
    print(-1)