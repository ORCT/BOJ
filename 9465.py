import sys
ssr = sys.stdin.readline

t = int(ssr())
for _ in range(t):
    n = int(ssr())
    sticker = [list(map(int, ssr().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]
    if n > 1:
        dp[0][1], dp[1][1] = dp[1][0]+sticker[0][1], dp[0][0]+sticker[1][1]
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2])+sticker[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2])+sticker[1][i]
    print(max(dp[0][-1], dp[1][-1]))
    
'''
선택한 거에서 대각선 아래거랑 그 놈의 대각선위의 합이랑, 그그놈의 아래놈을 비교해서 더 큰 놈을
선택한 놈이 2행이라면 대각위,대각아래 랑 그그위를 비교
for i in range(2):
for j in range(n):
max((i,j)+(i+1,j+1),(i+1,j)+(i,j+1))

그럼 i는 하나만 써도 될 듯
반복 필요없지 않나
재귀 써야하나
4개씩 묶어서 선택하면?

'''