'''
일단 녹는 치즈는 외부 공기와 2변이 닿아야 한다
근데 치즈로 외벽이 있는 경우 외벽 내에 공기가 있어도 내부 치즈는 녹지 않는다
외벽이 깨져서 외부 공기가 들어온다 치면 그 때부터는 녹는다

전형적인 그래프 탐색 문제인 것 같은데
아예 외부 공간, 그 외부 공간과 닿는 치즈, 치즈 벽 내의 공간, 그 외의 치즈
이렇게 4개로 분할해서 생각해야하나?

예를 들어 이런 경우는

 **     
 * ****
 *    *
 * ** *
 * ** *
 *    *
 ******
9 8
0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0
0 1 0 1 1 1 1 0
0 1 0 0 0 0 1 0
0 1 0 1 1 0 1 0
0 1 0 1 1 0 1 0
0 1 0 0 0 0 1 0
0 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0

8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0

처음에는 위에 두개랑 외곽 3개 사라지는데
그 다음에는 내부가 다 공기가 통해서 전부 사라짐

나이브한 구현
모든 좌표를 다 돌면서 외부 공간과 2변이 접하는 치즈를 찾아서 지우고 1초 증가
이걸 반복
근데 아마 이렇게 하면 시간초과가 나겠지?
최대 입력은 100*100이고 1초니까 C언어 기준 10억회라고 치면 10만번 정도는 전체 탐색을 해도 되네
4방향을 다 탐색해야하니까 25000번으로 줄어들겠네
만개가 다 치즈여도 25000번이면 충분히 돌겠는데
그럼 시간초과 없이 가능할지도?

녹인 치즈를 q에 추가한 다음에 outer_air를 돌려
그럼 치즈 외벽이 깨진 다음에 외부 공기랑 접촉하는 내부 공기에다가 bfs를 바로 쓸 수 있지

플로우
최초 외부 공기를 전부 2로 바꿔서 외부 공기와 내부 공기를 분리
녹일 치즈가 있는지 체크, 혹시 외부 공기랑 닿는 치즈를 따로 저장해뒀다가 쓰면 굳이 전부 탐색할 필요 없지 않나

'''

from collections import deque
import sys
ssr = sys.stdin.readline

def outer_air():
    nomis = []
    while q:
        r, c = q.popleft()
        for dr, dc in dpos:
            if 0 <= r+dr < n and 0 <= c+dc < m and visited[r+dr][c+dc] == False:
                if board[r+dr][c+dc] == 0:
                    q.append((r+dr, c+dc))
                    nomis.append((r+dr, c+dc))
                    visited[r+dr][c+dc] = True
                elif board[r+dr][c+dc] == 1:
                    cheese.add((r+dr, c+dc))
    for r, c in nomis:
        board[r][c] = 2
                        
def melt_cheese():
    nomis = []
    while len(cheese) > 0:
        r, c = cheese.pop()
        cnt = 0
        for dr, dc in dpos:
            if board[r+dr][c+dc] == 2:
                cnt += 1
        if cnt > 1:
            nomis.append((r, c))
            q.append((r, c))
    for r, c in nomis:
        board[r][c] = 2

n, m = map(int, ssr().split())
board = [list(map(int, ssr().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dpos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque([(0, 0)])
board[0][0] = 2
cheese = set([])
ans = 0
while True:
    outer_air()
    if len(cheese) == 0:
        print(ans)
        break
    else:
        melt_cheese()
        ans += 1