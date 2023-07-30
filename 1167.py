'''
일단은 인접행렬로 시작하자

1에서 출발해서 모든 노드까지의 거리를 재서 제일 큰 값을 반환하면 되겠다고 생각했는데
1을 사용하지 않았을 때 지름이 가장 큰 경우가 있을 수 있겠네
'''
from collections import deque
import sys
ssr = sys.stdin.readline

n = int(ssr())
adj_list = [[] for _ in range(n+1)]
for _ in range(n):
    line = list(map(int, ssr().split()))
    for i in range(1, len(line), 2):
        if line[i] != -1:
            adj_list[line[0]].append((line[i], line[i+1]))
q = deque([(1, 0)])
visited = [False for _ in range(n+1)]
visited[1] = True
start_node = 0
ans = 0
while q:
    cur_node, cur_dist = q.popleft()
    if ans < cur_dist:
        start_node, ans = cur_node, cur_dist
    for next_node, next_dist in adj_list[cur_node]:
        if visited[next_node] == False:
            q.append((next_node, cur_dist+next_dist))
            visited[next_node] = True
q.append((start_node, 0))
visited = [False for _ in range(n+1)]
visited[start_node] = True
while q:
    cur_node, cur_dist = q.popleft()
    ans = cur_dist if ans < cur_dist else ans
    for next_node, next_dist in adj_list[cur_node]:
        if visited[next_node] == False:
            q.append((next_node, cur_dist+next_dist))
            visited[next_node] = True
print(ans)