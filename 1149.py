import sys
ssr = sys.stdin.readline

n = int(ssr())
cost = [list(map(int, ssr().split())) for _ in range(n)]
min_cost = [[0,0,0] for _ in range(n)]
min_cost[0] = cost[0]
for i in range(1,n):
    min_cost[i][0] = min(min_cost[i-1][1], min_cost[i-1][2]) + cost[i][0]
    min_cost[i][1] = min(min_cost[i-1][0], min_cost[i-1][2]) + cost[i][1]
    min_cost[i][2] = min(min_cost[i-1][0], min_cost[i-1][1]) + cost[i][2]
print(min(min_cost[-1]))
'''
나눠지지 않는 가방문제와 비슷한 느낌
선택했던 열은 연속해서 못 뽑으니까 오히려 더 쉬울 수도 있음'''