'''
메모리 제한이 꽤 작은데 bfs로 풀지 말라는 뜻인가?
바로 메모리 제한

어떻게 하면 메모리 제한을 뺄 수 있을까 어차피 모든 조합을 다 해야하는데
재귀를 이용한 dfs로 풀어야 한다는 뜻일까
그것도 아닌거 같은게 n이 10만이면
맨왼쪽에서 출발하는 경우에도 이미 2의 10만제곱인데 오른쪽도 있고 가운데는 3의 10만이잖아

그리디가 가능하기가 힘들지
예를 들어서
123
099
099
099
000
000
000
900
900
900
900
이런 경우라면 처음에 3을 선택할게 아니라 2를 선택해서 아래에 있는 9를 다 먹어야 하니까

그리디가 되나?
뭔가 안될거 같은데

시작노드 각각 준다고 치고 그리디 돌리면 60만번이면 끝내지 않나?
한층씩 내려갈 때 마다 해당 위치에서 가질 수 있는 최적의 값만 저장하고 다른 루트는 없애는거지
어차피 방문 루트가 중요한 건 아니니까
'''

import sys
ssr = sys.stdin.readline

def max_dp():
    scores = [board[0][0], board[0][1], board[0][2]]
    dpos = (-1, 0, 1)
    for r in range(n):
        if r == n-1:
            break
        tmps = [i for i in scores]
        scores = [tmps[i]+board[r+1][i] for i in range(3)]
        for c in range(3):
            for dc in dpos:
                if 0 <= c+dc < 3:
                    scores[c+dc] = max(tmps[c]+board[r+1][c+dc], scores[c+dc])
    return max(scores)
                    
def min_dp():
    scores = [board[0][0], board[0][1], board[0][2]]
    dpos = (-1, 0, 1)
    for r in range(n):
        if r == n-1:
            break
        tmps = [i for i in scores]
        scores = [tmps[i]+board[r+1][i] for i in range(3)]
        for c in range(3):
            for dc in dpos:
                if 0 <= c+dc < 3:
                    scores[c+dc] = min(tmps[c]+board[r+1][c+dc], scores[c+dc])
    return min(scores)

n = int(ssr())
board = [list(map(int, ssr().split())) for _ in range(n)]
print(max_dp(), min_dp())