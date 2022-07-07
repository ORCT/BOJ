import heapq
import sys
ssr = sys.stdin.readline

n = int(ssr())
h=[]
for _ in range(n):
    o = int(ssr())
    if o == 0:
        if len(h) != 0:
            print(heapq.heappop(h)[1])
        else:
            print(0)
    else:
        heapq.heappush(h, (abs(o), o))