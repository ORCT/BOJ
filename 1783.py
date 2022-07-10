n,m = map(int, input().split())

if n >= 3:
    if m >= 7:
        print(m-2)
    elif m >= 4:
        print(4)
    else:
        print(m)
elif n == 2:
    if m >= 7:
        print(4)
    else:
        print(1+(m-1)//2)
else:
    print(1)