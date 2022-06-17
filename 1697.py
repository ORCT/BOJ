from collections import deque

n,k = map(int, input().split())
q = deque([[n,0]])
visited = [False for _ in range(100001)]
visited[n] = True
while 1:
    if n == k:
        print(0)
        break
    p = q.popleft()
    a = p[0]-1
    b = p[0]+1
    c = p[0]*2
    if a == k or b == k or c == k:
        print(p[1]+1)
        break
    else:
        if a>=0 and visited[a] == False:
            q.append([a,p[1]+1])
            visited[a] = True
        if b<=100000 and visited[b] == False:
            q.append([b,p[1]+1])
            visited[b] = True
        if c<=100000 and visited[c] == False:
            q.append([c,p[1]+1])
            visited[c] = True