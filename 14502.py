'''
벽은 무조건 3개를 세워야 함
빈공간은 최소 3개는 주어짐
바이러스는 2~10개 존재'''
from collections import deque
import copy
import sys
ssr = sys.stdin.readline

def bfs(n, m, board, twos):
    dpos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque(twos)
    while q:
        v_r, v_c = q.popleft()
        for dr, dc in dpos:
            pos_r, pos_c = v_r+dr, v_c+dc
            if 0 <= pos_r < n and 0 <= pos_c < m:
                if board[pos_r][pos_c] == 0:
                    board[pos_r][pos_c] = 2
                    q.append((pos_r, pos_c))
    zero_cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                zero_cnt += 1
    return zero_cnt
                
def func(n, m, board, zeros, twos):
    result = 0
    for i in range(len(zeros)-2):
        board[zeros[i][0]][zeros[i][1]] = 1
        for j in range(i+1, len(zeros)-1):
            board[zeros[j][0]][zeros[j][1]] = 1
            for k in range(j+1, len(zeros)):
                board[zeros[k][0]][zeros[k][1]] = 1
                tmp = bfs(n, m, copy.deepcopy(board), twos)
                if tmp > result:
                    result = tmp
                board[zeros[k][0]][zeros[k][1]] = 0
                
            board[zeros[j][0]][zeros[j][1]] = 0
            
        board[zeros[i][0]][zeros[i][1]] = 0
    return result

n, m = map(int, ssr().split())
board = [list(map(int, ssr().split())) for _ in range(n)]
viruses = []
spaces= []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            viruses.append((i, j))
        elif board[i][j] == 0:
            spaces.append((i, j))
ans = func(n, m, board, spaces, viruses)
print(ans)