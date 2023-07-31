'''from collections import deque
import sys
ssr = sys.stdin.readline

n = int(ssr())
m = int(ssr())
adj_dict = {i:[] for i in range(1,n+1)}
for _ in range(m):
    tmp = list(map(int, ssr().split()))
    adj_dict[tmp[0]].append((tmp[1],tmp[2]))
# print(adj_dict)
visited = [0 for _ in range(n+1)]
start, end = map(int, ssr().split())
q = deque([(start, 0)])
visited[1] = 1
ans = 100000
while q:
    tmp = q.popleft()
    if tmp[0] == end:
        ans = min(ans, tmp[1])
    for i in adj_dict[tmp[0]]:
        q.append((i[0], tmp[1]+i[1]))
        visited[i[0]] = 1
print(ans)'''
'''
참고로 위 풀이(bfs)는 메모리초과가 났다.
데이크스트라에 대해서 알아보자

전형적인 데이크스트라 문제다
간선과 간선의 길이 또는 비용이 주어지고'''

import heapq
import sys
ssr = sys.stdin.readline
INF = 100000000

def dijkstra(start, arrive):
    min_cost = [INF for _ in range(n+1)]
    h = []
    heapq.heappush(h, (0, start)) # 거리, 도착 순서
    min_cost[start] = 0
    while h:
        now_cost, now = heapq.heappop(h) # 거리, 도착 순서
        if now_cost > min_cost[now]:
            continue
        for after_cost, after in bus[now]:
            if min_cost[now]+after_cost < min_cost[after]:
                min_cost[after] = min_cost[now] + after_cost
                heapq.heappush(h, (min_cost[after], after))
    print(min_cost[arrive])

n = int(ssr())
m = int(ssr())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, ssr().split())
    bus[a].append((c, b))
start, arrive = map(int, ssr().split())
dijkstra(start, arrive)