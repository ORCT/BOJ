n = int(input())
ans = 1
for i in range(1,n+1):
    ans *= i
ans = list(str(ans))
cnt = 0
while 1:
    if ans[len(ans)-1] != '0':
        print(cnt)
        break
    else:
        ans.pop()
        cnt += 1