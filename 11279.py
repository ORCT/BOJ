import heapq
import sys
ssr = sys.stdin.readline

n = int(ssr())
h = []
for _ in range(n):
    a = int(ssr())
    if a > 0:
        heapq.heappush(h,-a)
    else:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h))