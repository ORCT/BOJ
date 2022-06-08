n = int(input())
t = [0 for _ in range(301)]
s = [0 for _ in range(301)]
for i in range(1,n+1):
    s[i]=int(input())
t[1],t[2] = s[1],s[1]+s[2]
for i in range(3,n+1):
    t[i] = max(s[i]+s[i-1]+t[i-3],s[i]+t[i-2])
print(t[n])