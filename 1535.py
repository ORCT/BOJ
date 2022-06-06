n = int(input())
p = [0]
h = [0]
p.extend(list(map(int, input().split())))
h.extend(list(map(int, input().split())))
t = [[0 for _ in range(101)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(101):
        if j<p[i]:
            t[i][j] = t[i-1][j]
        else:
            t[i][j] = max(h[i]+t[i-1][j-p[i]], t[i-1][j])
print(t[n][99])