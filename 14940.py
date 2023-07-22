from collections import deque
import sys

ssr = sys.stdin.readline

def get_pos():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                visited[i][j] = 0
                q.append((i, j, 0))
            elif board[i][j] == 0:
                visited[i][j] = 0

def bfs():
    while q:
        r, c, d = q.popleft()
        if 0 <= r-1:
            if visited[r-1][c] == -1:
                if board[r-1][c] == 1:
                    visited[r-1][c] = d+1
                    q.append((r-1, c, d+1))
                else:
                    visited[r-1][c] = 0
        if 0 <= c-1:
            if visited[r][c-1] == -1:
                if board[r][c-1] == 1:
                    visited[r][c-1] = d+1
                    q.append((r, c-1, d+1))
                else:
                    visited[r][c-1] = 0
        if r+1 < n:
            if visited[r+1][c] == -1:
                if board[r+1][c] == 1:
                    visited[r+1][c] = d+1
                    q.append((r+1, c, d+1))
                else:
                    visited[r+1][c] = 0
        if c+1 < m:
            if visited[r][c+1] == -1:
                if board[r][c+1] == 1:
                    visited[r][c+1] = d+1
                    q.append((r, c+1, d+1))
                else:
                    visited[r][c+1] = 0

n, m = map(int, ssr().split())
visited = [[-1 for _ in range(m)] for _ in range(n)]
board = [list(map(int, ssr().split())) for _ in range(n)]
q = deque([])
get_pos()
bfs()
for i in visited:
    print(*i)