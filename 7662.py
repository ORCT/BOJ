import heapq
import sys
ssr = sys.stdin.readline

t = int(ssr())
for _ in range(t):
    minh, maxh = [], []
    k = int(ssr())
    visited = [False for _ in range(k)]
    for i in range(k):
        c = ssr().split()
        if c[0] == 'I':
            heapq.heappush(minh, (int(c[1]), i))
            heapq.heappush(maxh, (-int(c[1]), i))
        else:
            if c[1] == '1':
                if len(maxh) == 0:
                    continue
                else:
                    while maxh:
                        if visited[maxh[0][1]] == True:
                            heapq.heappop(maxh)
                        else:
                            a = heapq.heappop(maxh)
                            visited[a[1]] = True
                            break
            else:
                if len(minh) == 0:
                    continue
                else:                
                    while minh:
                        if visited[minh[0][1]] == True:
                            heapq.heappop(minh)
                        else:
                            a = heapq.heappop(minh)
                            visited[a[1]] = True
                            break
    while maxh:
        if visited[maxh[0][1]] == True:
            heapq.heappop(maxh)
        else:
            break
    while minh:
        if visited[minh[0][1]] == True:
            heapq.heappop(minh)
        else:
            break
    if len(minh) == 0 or len(maxh) == 0:
        print('EMPTY')
    else:
        print(-maxh[0][0],minh[0][0])