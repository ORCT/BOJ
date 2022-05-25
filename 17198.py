from collections import deque

def bfs(r,c):
    q = deque()
    q.append((r,c))
    t[r][c]=0
    while q:
        r,c = q.popleft()
        for dr,dc in d:
            R,C = r+dr, c+dc
            if 0<=R<10 and 0<=C<10:
                if t[R][C] == 'L':
                    return t[r][c]
                if t[R][C] == '.':
                    q.append((R,C))
                    t[R][C] = t[r][c]+1

t = [list(input()) for _ in range(10)]#공백 아니어도 split
d = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(10):
    for j in range(10):
        if t[i][j] == 'B':
            cnt = bfs(i,j)
print(cnt)