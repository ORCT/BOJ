import sys
ssr = sys.stdin.readline

n = int(ssr())
t = [list(map(int, ssr().split())) for _ in range(n)]
dp = [[0]*(i+1) for i in range(n)]
dp[0][0] = t[0][0]
for i in range(1,n):
    for j in range(i):
        dp[i][j] = max(dp[i-1][j]+t[i][j], dp[i][j])
        dp[i][j+1] = dp[i-1][j]+t[i][j+1]
print(max(dp[-1]))