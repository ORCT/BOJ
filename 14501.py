from collections import deque

n = int(input())
t = {n+1:(16,16)}
q = deque([(1, 0)])
ans = []
for i in range(1, n+1):
    a, b = map(int, input().split())
    t[i] = (a, b)
while q:
    tmp = q.popleft()
    c, d = t[tmp[0]]
    if tmp[0]+c <= n+1:
        q.append((tmp[0]+c, tmp[1]+d))
    else:
        ans.append(tmp[1])
    if tmp[0]+1 <= n+1:
        q.append((tmp[0]+1, tmp[1]))
    else:
        ans.append(tmp[1])
print(max(ans))