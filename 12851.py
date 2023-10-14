from collections import deque

n, k = map(int, input().split())
visited = [0 for _ in range(200001)]
visited[n] = 1
q = deque([(n, 0)])
ans = 100001
methods = []
while q:
    cur_pos, cur_time = q.popleft()
    if cur_pos == k:
        methods.append(cur_time)
        if ans > cur_time:
            ans = cur_time
    else:
        dpos = [cur_pos-1, cur_pos+1, cur_pos*2]
        for i in dpos:
            if 0 <= i <= 200000 and visited[i] <= 3:
                q.append((i, cur_time+1))
                visited[i] += 1
print(ans)
print(methods.count(ans))