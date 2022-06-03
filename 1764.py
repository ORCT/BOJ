import sys
ssr = sys.stdin.readline
n,m = map(int, ssr().split())
d = {ssr():i for i in range(n)}
name = []
for _ in range(m):
    a = ssr()
    if a in d.keys():
        name.append(a.rstrip())
print(len(name))
name.sort()
for i in range(len(name)):
    print(name[i])