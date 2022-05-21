k,n = map(int,input().split())
if n == 1:
    print(-1)
else:
    result = (-k*n)//(1-n)
    if (-k*n)%(1-n):
        print(result+1)
    else:
        print(result)