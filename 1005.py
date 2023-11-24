'''
약간 후위 순회 트리 같은 느낌?
특정 건물을 짓기 전에 먼저 지어야 하는 건물이 존재함
'걔들을 짓는데 걸리는 시간 + 타겟 건물 짓는 시간' 이 요구 사항
dfs로 타고 가서 같은 부모를 가진 건물의 건축 시간을 다 모아서 그 중에 최댓값만 더하든지
'''

import sys; ssr = sys.stdin.readline
sys.setrecursionlimit(10000)

def f(node):
    if dp_delay[node] == -1: # 아직 계산이 안됐고, 자식이 존재하는 노드
        results = [] # 자식들 값 계산해서 반환 받은거, 여기서 최댓값이랑 자기 자신 딜레이랑 합칠거임
        for child in build[node]: # 자식들 반복문 돌리면서 재귀로 가볼거임
            child_delay = f(child)
            results.append(child_delay)
        dp_delay[node] = delays[node] + max(results)
    return dp_delay[node]
    
t = int(ssr())
for _ in range(t):
    n, k = map(int, ssr().split())
    delays = [0] + list(map(int, ssr().split()))
    dp_delay = delays[:] # deepcopy
    build = [[] for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, ssr().split())
        build[y].append(x)
        if dp_delay[y] != -1: # 초기화를 자기 자신의 딜레이로 한 다음에 선행조건이 있는 건물만 -1로 바꾸기
            dp_delay[y] = -1
    tar = int(ssr())
    ans = f(tar)
    print(ans)