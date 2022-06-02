t = [-1 for _ in range(100001)]
t[2],t[4],t[5],t[6],t[7],t[8] = 1,2,1,3,2,4
for i in range(9,100001):
    t[i] = min((t[i-2]+t[2]),(t[i-5]+t[5]))
print(t[int(input())])