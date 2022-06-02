import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = {i:input().rstrip() for i in range(1,n+1)}
t = dict(map(reversed, d.items()))
for _ in range(m):
    a = input().rstrip()
    if not a[0].isdigit():
        print(t[a])
    else:
        print(d[int(a)])