'''
착지점 기준 m 만큼 움직일 수 있음
착지점은 하나씩 반복문으로 다 돌려봐야 함
그 중에서 최댓값
'''

'''
# dijkstra

import sys; ssr = sys.stdin.readline
import heapq
INF = 16

n, m, r = map(int, ssr().split())
items = list(map(int, ssr().split()))
routes = [[] for _ in range(n+1)]
ans = 0
for _ in range(r):
    a, b, l = map(int, ssr().split())
    routes[a].append((b, l))
    routes[b].append((a, l))
for start in range(1, n+1):
    q = [(0, start)]
    min_dist = [INF for _ in range(n+1)]
    min_dist[start] = 0
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        if cur_dist > min_dist[cur_node]:
            continue
        for next_node, next_dist in routes[cur_node]:
            dist = cur_dist + next_dist
            if dist < min_dist[next_node]:
                min_dist[next_node] = dist
                heapq.heappush(q, (dist, next_node))
    item_cnt = 0
    min_dist = min_dist[1:]
    for i in range(len(min_dist)):
        if min_dist[i] <= m:
            item_cnt += items[i]
    if item_cnt > ans:
        ans = item_cnt
print(ans)'''

# floyd-warshall

import sys; ssr = sys.stdin.readline
INF = 16

n, m, r = map(int, ssr().split())
items = list(map(int, ssr().split()))
routes = [[] for _ in range(n+1)]
min_dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, ssr().split())
    routes[a].append((b, l))
    routes[b].append((a, l))
    min_dist[a][b] = min(min_dist[a][b], l)
    min_dist[b][a] = min(min_dist[b][a], l)
for i in range(n+1):
    min_dist[i][i] = 0
for mid in range(n+1):
    for start in range(n+1):
        for end in range(n+1):
            min_dist[start][end] = min(min_dist[start][end], min_dist[start][mid]+min_dist[mid][end])
ans = 0
for i in range(n+1):
    tmp = 0
    for j in range(n+1):
        if min_dist[i][j] <= m:
            tmp += items[j-1]
    if ans < tmp:
        ans = tmp
print(ans)