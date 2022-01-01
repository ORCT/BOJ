import sys
ssr = sys.stdin.readline

n = int(ssr())
d = [0 for _ in range(1,1000001)]
for i in range(1,n+1):
    d[i] = d[i-1]+1
    if i%2 == 0: d[i] = min(d[i],d[int(i/2)]+1)
    if i%3 == 0: d[i] = min(d[i],d[int(i/3)]+1)
print(d[n]-1)