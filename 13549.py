'''
n이 k보다 큰 값이 나올 수 있음
k보다 큰 값으로 넘어가서 내려오는게 더 빠른 경우가 있음
'''

import heapq
import sys
ssr = sys.stdin.readline

INF = 100001

def dijkstra(n, k): # -1, 1, *2
    h = [(0, n)]
    time = [INF for _ in range(200001)]
    time[n] = 0
    while h:
        cur_time, cur_node = heapq.heappop(h)
        if cur_time > time[cur_node]:
            continue
        if 0 <= cur_node-1 and time[cur_node]+1 < time[cur_node-1]:
            time[cur_node-1] = time[cur_node]+1
            heapq.heappush(h, (time[cur_node]+1, cur_node-1))
        if cur_node+1 <= 100000 and time[cur_node]+1 < time[cur_node+1]:
            time[cur_node+1] = time[cur_node]+1
            heapq.heappush(h, (time[cur_node]+1, cur_node+1))
        if 2*cur_node <= 200001 and time[cur_node] < time[2*cur_node]:
            time[2*cur_node] = time[cur_node]
            heapq.heappush(h, (time[cur_node], 2*cur_node))
    print(time[k])
        
n, k = map(int, ssr().split())
dijkstra(n, k)