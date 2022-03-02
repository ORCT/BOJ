import sys
ssr = sys.stdin.readline

k = int(ssr())
res = []
for i in range(k):
    num = int(ssr())
    if num == 0:
        res.pop()
    else:
        res.append(num)
print(sum(res))