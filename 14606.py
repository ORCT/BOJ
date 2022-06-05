import math
n = int(input())
t = [0 for _ in range(n+1)]
t[1] = 0
for i in range(2,n+1):
    t[i] = math.ceil(i/2)*(i-math.ceil(i/2)) + t[math.ceil(i/2)] + t[i-math.ceil(i/2)]
print(t[n])