t = int(input())
b= [300,60,10]
ans=[]
if t%10 != 0:
    print(-1)
else:
    for i in range(3):
        cnt = 0
        cnt += t//b[i]
        t = t%b[i]
        ans.append(cnt)
print(*ans)