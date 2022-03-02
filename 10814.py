import sys
ssr = sys.stdin.readline

n = int(ssr())
member = []
for i in range(n):
    member.append(ssr().split())
member.sort(key = lambda x : int(x[0]))
for i in range(n):
    print(*member[i])