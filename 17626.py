import math

t = [0 for _ in range(50001)]
t[0],t[1],t[2],t[3]=0,1,2,3
for i in range(4,50001):
    minv=5
    a = math.floor(math.sqrt(i))
    for j in range(1,a+1):
        minv = min(minv, t[i-j**2]+1)
    t[i] = minv
print(t[int(input())])