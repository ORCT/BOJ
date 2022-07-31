import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
num = [list(map(int, ssr().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][0] = num[i][0]
    for j in range(1,n):
        dp[i][j] += num[i][j] + dp[i][j-1]
for _ in range(m):
    x1,y1,x2,y2 = map(int, ssr().split())
    ans = 0
    for i in range(x1-1,x2):
        if y1-2 < 0:
            ans += dp[i][y2-1]
        else:
            ans += dp[i][y2-1] - dp[i][y1-2]
    print(ans)
    # print(dp[x2-1][y2-1]-dp[x1-1][y1-1])
# print(dp)
'''ans = list[x2][y2] - list[x1][y1] 의 형태가 될 것
각 행별로 누적되도록 작성
즉 이것은 '''
