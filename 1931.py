import sys
ssr = sys.stdin.readline

n = int(ssr())
c = [list(map(int, ssr().split())) for _ in range(n)]
c.sort(key= lambda x:(x[1], x[0]))
cnt = 1
end = c[0][1]
for i in range(1, n):
    if c[i][0] >= end:
        cnt += 1
        end = c[i][1]
print(cnt)