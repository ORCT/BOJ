n = int(input())
if n == 1 or n == 2 or n == 3:
    print(n)
else:
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%15746
    print(dp[n])