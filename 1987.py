'''
단순한 그래프 탐색이 아니라 탐색 순서가 좀 중요하네
미리가서 방문처리를 해버리면 열심히 카운트 올려서 온 친구가 더 이상 진행을 못하는 일이 생긴다

예전에 벽 부수는 문제에서 이거랑 비슷하게 이미 방문처리를 해버린 노드에 접근을 못하는 문제가 있었는데
그 때는 visited를 1과 2의 두가지로 갱신하는 방법으로 벽을 부수지 않고 온 친구가 포텐셜이 있다고 생각해서
벽을 안부수고 왔으면 이미 갔던 노드라도 갈 수 있게 했었음

근데 이번에는 어떻게 구분을 할 수 있을까
저 멀리서 부터 뺑뻉 돌아온 친구라는 구분을 어떻게 할 수가 있을까
간단하게 할 수 있는건 cnt가 더 크면
아 가능하려나?
아니지 알파벳 중복도 체크하는데 cnt가 커도 이미 갔던 칸은 중복처리를 해놨으니까
근데 방문처리를 할 필요가 있나? 이미 알파벳 중복 체크 때문에 갔던 곳을 다시 못가지 않나

방문 순서에 따라 방문처리를 다르게 해야할 때는 어떻게 하면 좋을까~
dfs로 하면 그런 부분을 해결할 수 있나?
시간초과가 나네

즉, dfs로 모든 경로를 다 가보면서 여기는 안되네 싶은 방법은 안된다는 건데,
아예 불가능한 위치를 따로 저장하는 건 어떨까.
예를 들어서 시작점이 C인데 어떤 위치가 진입 루트 A, 가운데 B 나머지 3방향이 C라면
해당 B 위치에 들어가면 아예 시도를 해볼 필요가 없도록
'''

import string
import sys
ssr = sys.stdin.readline

def dfs(r, c, cnt):
    global ans
    if visited[board[r][c]] == 1:
        ans = max(ans, cnt)
        return
    else:
        visited[board[r][c]] = 1
        for dr, dc in dpos:
            if 0 <= r+dr < R and 0 <= c+dc < C:
                dfs(r+dr, c+dc, cnt+1)
        visited[board[r][c]] = 0
        
def dfs_stack():
    global ans
    s = [(0, 0, board[0][0])]
    while s:
        r, c, path = s.pop()
        if len(path) > ans:
            ans = len(path)
        if len(path) == 26:
            break
        for dr, dc, in dpos:
            if 0 <= r+dr < R and 0 <= c+dc < C and board[r+dr][c+dc] not in path:
                s.append((r+dr, c+dc, path+board[r+dr][c+dc]))
        
R, C = map(int, ssr().split())
visited = {i:0 for i in string.ascii_uppercase}
board = [ssr().rstrip() for _ in range(R)]
dpos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
dfs_stack()
print(ans)