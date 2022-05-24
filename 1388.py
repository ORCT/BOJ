def dfs(r,c):
    global cnt
    if visited[r][c] == True:
        return
    visited[r][c] = True
    if b[r][c] == '-':
        if c+1<m and b[r][c+1] == '-':
            dfs(r,c+1)
        else:
            cnt += 1
    else:
        if r+1<n and b[r+1][c] == '|':
            dfs(r+1,c)
        else:
            cnt += 1
    
n,m = map(int, input().split())
b = [input() for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        dfs(i,j)
print(cnt)
#방문 여부를 따지긴 해야할듯
#방문여부 처리하고 재귀까지 완료했고 이제 어떻게 카운트를 셀 것인지가 중요한데
#다중 조건에서 무슨 조건을 먼저 쓰는지도 영향을 미치더라