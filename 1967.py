from collections import deque
import sys
ssr = sys.stdin.readline

n = int(ssr())
adj_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    line = list(map(int, ssr().split()))
    adj_list[line[0]].append((line[1], line[2]))
    adj_list[line[1]].append((line[0], line[2]))
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