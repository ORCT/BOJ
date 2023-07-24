from collections import deque
import sys
ssr = sys.stdin.readline

def check_pos():
    p_cnt = 0
    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                q.append((i, j))
                campus[i][j] = 'X'
            elif campus[i][j] == 'P':
                p_cnt += 1
    return p_cnt
                
def bfs():
    ans = 0
    while q:
        r, c = q.popleft()
        for dr, dc in dir:
            if 0 <= r+dr < n and 0 <= c+dc < m and campus[r+dr][c+dc] != 'X':
                if campus[r+dr][c+dc] == 'P':
                    ans += 1
                q.append((r+dr, c+dc))
                campus[r+dr][c+dc] = 'X'
    return ans                       
                
n, m = map(int, ssr().split())
campus = [list(ssr().rstrip()) for _ in range(n)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque([])
p_cnt = check_pos()
ans = bfs()
print(ans if ans != 0 else 'TT')