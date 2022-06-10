t = [0 for _ in range(101)]
t[1],t[2] = 1,1
for i in range(3,101):
    t[i] = t[i-2]+t[i-3]
n = int(input())
for _ in range(n):
    print(t[int(input())])