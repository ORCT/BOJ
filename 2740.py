n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m,k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]
c = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        for h in range(k):
            c[i][h] += a[i][j]*b[j][h]
for i in c:
    print(*i)
#n,k