t = int(input())
for _ in range(t):
    m,n,x,y = map(int, input().split())
    a,b = 0,0
    ans = 0
    for i in range(m+abs(m-n)):
        if (i*m+x-1)%n == y-1:
            ans = i*m+x
            break
    if ans == 0:
        print(-1)
    else:
        print(ans)
        
'''t = int(input())
for _ in range(t):
    m,n,x,y = map(int, input().split())
    '''