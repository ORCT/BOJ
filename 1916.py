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
참고로 위 풀이는 메모리초과가 났다
데이크스트라'''

import sys
ssr = sys.stdin.readline

n = int(ssr())
m = int(ssr())
adj_dict = {i:[] for i in range(1,n+1)}
for _ in range(m):
    tmp = list(map(int, ssr().split()))
    adj_dict[tmp[0]].append((tmp[1], tmp[2]))
start, end = map(int, ssr().split())
visited = [0 for _ in range(n+1)]
t = [100001 for _ in range(n+1)]
while 1:
    for i in adj_dict[start]:
        if visited[i] == 0 and t[i]