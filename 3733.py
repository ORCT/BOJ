while 1:
    try:
        n,s = map(int, input().split())
        x = s//(n+1)
        print(x)
    except:
        break