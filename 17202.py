a = input()
b = input()
t = []
for i in range(8):
    t.append(a[i])
    t.append(b[i])
ans = ''.join(t)
while 1:
    t=[]
    for i in range(len(ans)-1):
        t.append(str((int(ans[i])+int(ans[i+1]))%10))
    ans = ''.join(t)
    if len(ans)==2:
        break
print(ans)