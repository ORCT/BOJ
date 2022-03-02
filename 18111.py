import sys
ssr = sys.stdin.readline

n,m,b = map(int, ssr().split())
board = [list(map(int, ssr().split())) for _ in range(n)]
h = [i for i in range(257)]
result = []
for i in h:
    two = 0
    one = 0
    for j in range(n):
        for k in range(m):
            if board[j][k] >= i:
                two += board[j][k] - i
            else:
                one += board[j][k] - i
    if b+two+one >= 0:
        result.append([two*2 - one, i])
result.sort(key=lambda x:(x[0],-x[1]))
print(*result[0])