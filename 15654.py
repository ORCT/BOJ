import sys
ssr = sys.stdin.readline

def sol(num_len):
    if num_len == m:
        print(*ans)
        return
    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        ans.append(num[i])
        sol(num_len + 1)
        ans.pop()
        visited[i] = 0
    return

n,m = map(int, ssr().split())
num = list(map(int, ssr().split()))
visited = [0 for _ in range(n)]
num.sort()
for i in range(n):
    ans = [num[i]]
    visited[i] = 1
    sol(1)
    visited[i] = 0