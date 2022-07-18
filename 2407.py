n,m = map(int, input().split())
t = [0 for _ in range(101)]
t[1] = 1
for i in range(2, 101):
    t[i] = i*t[i-1]
print(t[n]//t[n-m]//t[m])