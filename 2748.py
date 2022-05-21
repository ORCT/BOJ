t=[0 for _ in range(91)]
t[0],t[1]=0,1
for i in range(2,91):
    t[i] = t[i-1]+t[i-2]
print(t[int(input())])