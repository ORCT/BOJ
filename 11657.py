import sys
ssr = sys.stdin.readline

INF = 5000001

def bellman_ford():
    for i in range(n):
        for cur_node, next_node, next_time in routes:
            if min_time[cur_node] != INF and min_time[cur_node]+next_time < min_time[next_node]:
                min_time[next_node] = min_time[cur_node]+next_time
                if i == n-1:
                    return False
    return True
       
n, m = map(int, ssr().split())
routes = [list(map(int, ssr().split())) for _ in range(m)]
min_time = [INF for _ in range(n+1)]
min_time[1] = 0
result = bellman_ford()
if result:
    for i in min_time[2:]:
        if i != INF:
            print(i)
        else:
            print(-1)
else:
    print(-1)