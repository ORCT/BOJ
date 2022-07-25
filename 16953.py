from collections import deque

a,b = map(int, input().split())
q = deque([(a,0)])
ans = -1
while q:
    tmp = q.popleft()
    if tmp[0] == b:
        ans = tmp[1]+1
        break
    val1, val2 = tmp[0]*2, int(str(tmp[0])+'1')
    if val1 <= b:
        q.append((val1, tmp[1]+1))
    if val2 <= b:
        q.append((val2, tmp[1]+1))
print(ans)