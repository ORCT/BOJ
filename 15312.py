t = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
tt = []
ans = []
h = input()
s = input()

for i in range(len(h)):
    tt.append(t[a.index(h[i])])
    tt.append(t[a.index(s[i])])
while 1:
    ans=[]
    for i in range(len(tt)-1):
        ans.append((tt[i]+tt[i+1])%10)
    tt = ans
    if len(ans) == 2:
        break
print(str(ans[0])+str((ans[1])))