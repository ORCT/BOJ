t = int(input())
table = [[0 for _ in range(30)] for _ in range(30)]
for i in range(1,30):
    table[1][i] = i
    table[i][i] = 1
for i in range(2,30):
    for j in range(i+1,30):
        table[i][j] = table[i][j-1]+table[i-1][j-1]
for _ in range(t):
    n,m = map(int, input().split())
    print(table[n][m])