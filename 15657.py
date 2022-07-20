import sys
ssr = sys.stdin.readline

def sol(idx):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(idx,n):
        ans.append(num[i])
        sol(i)
        ans.pop()
    return    

n,m = map(int, ssr().split())
num = list(map(int, ssr().split()))
num.sort()
for i in range(n):
    ans = [num[i]]
    sol(i)