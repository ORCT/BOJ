from collections import deque
import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
ls = [list(map(int, ssr().split())) for _ in range(n+m)]
visited = [0 for _ in range(101)]
q=deque([(1,0)])
visited[1] = 1
while q:
    tmp = q.popleft()
    if tmp[0] == 100:
        print(tmp[1])
        break
    for i in range(1,7):
        pos = tmp[0]+i
        if pos > 100:
            break
        else:
            for j in ls:
                if pos == j[0]:
                    pos = j[1]
                    break
            if visited[pos] == 0:
                q.append((pos, tmp[1]+1))
                visited[pos] = 1