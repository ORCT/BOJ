t = [0 for _ in range(1001)]
t[1],t[2],t[3] = 1,2,3
for i in range(4,1001):
    t[i] = t[i-1]+t[i-2]
print(t[int(input())]%10007)