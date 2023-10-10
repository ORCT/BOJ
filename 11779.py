import heapq
import sys
ssr = sys.stdin.readline
INF = 1000000001

def dijkstra(start, end):
    min_costs = [INF for _ in range(n+1)]
    min_costs[start] = 0
    min_route = [0 for _ in range(n+1)]
    min_route[start] = start
    h = [(0, start, str(start))]
    while h:
        cur_cost, cur_city, path = heapq.heappop(h)
        if cur_cost > min_costs[cur_city]:
            continue
        for next_cost, next_city in routes[cur_city]:
            costs = next_cost + cur_cost
            if costs < min_costs[next_city]:
                min_costs[next_city] = costs
                heapq.heappush(h, (costs, next_city, path+' '+str(next_city)))
                min_route[next_city] = cur_city
    return min_costs[end], min_route

def get_ans_route(cur_node, min_route, ans):
    ans.append(cur_node)
    if min_route[cur_node] == cur_node:
        return ans[::-1]
    else:
        return get_ans_route(min_route[cur_node], min_route, ans)
         
n = int(ssr())
m = int(ssr())
routes = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, ssr().split())
    routes[s].append((c, e))
tar_s, tar_e = map(int, ssr().split())
ans_cost, min_route = dijkstra(tar_s, tar_e)
ans_route = get_ans_route(tar_e, min_route, [])
print(ans_cost)
print(len(ans_route))
print(*ans_route)