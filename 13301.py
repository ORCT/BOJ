n = int(input())
if n == 1:
    print(4)
else:
    t = [0 for _ in range(81)]
    t[0],t[1] = 1,1
    for i in range(2,81):
        t[i] = t[i-1]+t[i-2]
    print(2*t[n-1]+2*(t[n-1]+t[n-2]))