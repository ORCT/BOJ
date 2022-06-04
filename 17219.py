import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = {}
for _ in range(n):
    a,b = map(str, input().rstrip().split())
    d[a] = b
for _ in range(m):
    print(d[input().rstrip()])