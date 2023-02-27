import sys
ssr = sys.stdin.readline

n = int(ssr())
hc = sorted(list(map(int, ssr().split())))
m = int(ssr())
nc = list(map(int, ssr().split()))
ans = [0 for _ in range(m)]

for i in range(m):
    start = 0
    end = n
    while start < end:
        mid = (start+end)//2
        if nc[i] == hc[mid]:
            ans[i] = 1
            break
        elif nc[i] < hc[mid]:
            end = mid
        else:
            start = mid + 1
print(*ans)