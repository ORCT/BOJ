import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
r = [list(ssr().rstrip()) for _ in range(n)]
s = n if n<m else m
ans = 1
for i in range(1,s):
    for j in range(n-i):
        for k in range(m-i):
            check = int(r[j][k])
            if int(r[j+i][k]) == check and int(r[j][k+i]) == check and int(r[j+i][k+i]) == check:
                ans = (i+1)**2
print(ans)