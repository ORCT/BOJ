'''import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
num = list(map(int, ssr().split()))
t = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    t[i+1][i+1] = num[i]
for i in range(n):
    for j in range(i+1,n):
        t[i+1][j+1] = t[i+1][j]+num[j]
for i in range(n):
    t[i+1][i+1] = num[i]
for _ in range(m):
    a,b = map(int, ssr().split())
    print(t[a][b])'''
    
import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
num = [0] + list(map(int, ssr().split()))
t = [0 for _ in range(n+1)]
for i in range(1,n+1):
    t[i] = t[i-1] + num[i]
for _ in range(m):
    a,b = map(int, ssr().split())
    print(t[b]-t[a-1])
