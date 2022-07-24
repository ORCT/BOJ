import sys
ssr = sys.stdin.readline

def sol(idx):
    if len(ans) == m:
        print(*ans)
        return
    last = 0
    for i in range(idx,n):
        if last != num[i]:
            ans.append(num[i])
            last = num[i]
            sol(i)
            ans.pop()
        
n,m = map(int, ssr().split())
num = sorted(list(map(int, ssr().split())))
ans = []
sol(0)