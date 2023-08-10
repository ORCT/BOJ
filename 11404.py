'''
플로이드-워셜
모든 노드 간 최단거리

min_cost의 원소가 갖는 의미
i도시에서 j도시로 가는 최단거리

갈 수 없는 경우에도 0을 출력하라는데?

O(n^3)짜리 알고리즘
반복문의 순서는 중간, 시작, 도착
'''

import sys
ssr = sys.stdin.readline

INF = 10000001

n = int(ssr())
m = int(ssr())
min_cost = [[INF for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, ssr().split())
    min_cost[a-1][b-1] = min(min_cost[a-1][b-1], c)
for i in range(n):
    min_cost[i][i] = 0
for middle_node in range(n):
    for start_node in range(n):
        for end_node in range(n):
            min_cost[start_node][end_node] = min(min_cost[start_node][end_node], min_cost[start_node][middle_node]+min_cost[middle_node][end_node])
for i in min_cost:
    print(*[j if j != INF else 0 for j in i])