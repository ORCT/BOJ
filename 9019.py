from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a,b = input().split()
    b = '0'*(4-len(b)) + b
    visited = [0 for _ in range(10000)]
    q = deque([(a,'')])
    visited[int(a)] = 1
    while q:
        tmp = q.popleft()
        tmp1 = '0'*(4-len(tmp[0])) + tmp[0]
        if tmp1 == b:
            ans = tmp[1]
            break
        else:
            d = int(tmp1)*2%10000
            if visited[d] == 0:
                q.append((str(d),tmp[1]+'D'))
                visited[d] = 1
            s = int(tmp1)-1 if int(tmp1)-1 >= 0 else 9999
            if visited[s] == 0:
                q.append((str(s),tmp[1]+'S'))
                visited[s] = 1
            l = tmp1[1:]+tmp1[0]
            if visited[int(l)] == 0:
                q.append((l,tmp[1]+'L'))
                visited[int(l)] = 1
            r = tmp1[3]+tmp1[0:3]
            if visited[int(r)] == 0:
                q.append((r,tmp[1]+'R'))
                visited[int(r)] = 1
    print(ans)