n = int(input())
t = [[] for _ in range(n+1)]
t[0] = [1,0]
for i in range(1,n+1):
    t[i] = [t[i-1][1],t[i-1][0]+t[i-1][1]]
print(*t[n])