import sys
ssr = sys.stdin.readline

n = int(ssr())
ans = list(ssr().rstrip())
for _ in range(n-1):
    tmp = list(ssr().rstrip())
    for i in range(len(tmp)):
        if ans[i] != tmp[i]:
            ans[i] = '?'
print(''.join(ans))