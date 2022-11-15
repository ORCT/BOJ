'''while 1:
    try:
        a,b,c = map(int, input().split())
        print(max(b-a-1, c-b-1))
    except:
        break'''

while 1:
    try:
        ans = 0
        a,b,c = map(int, input().split())
        while 1:
            if b-a <= 1 and c-b <= 1:
                print(ans)
                break
            if b-a > c-b:
                c = b-1
                c, b = b, c
                ans += 1
            else:
                a = b+1
                b,a = a,b
                ans += 1
    except:
        break