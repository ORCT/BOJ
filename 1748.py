'''s = ''
for i in range(1,int(input())+1):
    s += str(i)
print(len(s))'''

n = int(input())
num = [100000000,10000000,1000000,100000,10000,1000,100,10,1]
ans = 0
for i in num:
    if n-i>=0:
        ans += (n-i+1)*len(str(i))
        n = int('9'*(len(str(i-1))))
print(ans)