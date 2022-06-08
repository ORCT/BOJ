t = [0 for _ in range(10001)]
t[1],t[2] = 1,1
for i in range(3,10001):
    t[i] = t[i-1]+t[i-2]
print(t[int(input())])