c,r = map(int, input().split())
k = int(input())
s = 0
shell = [0]
while 1:
    a = ((c-1-2*s)+(r-1-2*s))*2
    if a > 0:
        shell.append(a + shell[-1])
        s += 1
    else:
        break
if c*r < k :
    print(0)
else:
    r_start = 0
    c_start = 0
    for i in range(1, len(shell)):
        if k <= shell[i]:
            k -= shell[i-1]
            r_start, c_start = i-1, i-1
            c = c-2*(i-1)
            r = r-2*(i-1)
            break
    if k <= r:
        print(1 + c_start, r_start + k)#1
    elif k < r+c:
        print(1 + c_start - r + k, r_start + r)#2
    elif k < 2*r + c - 1:
        print(c_start + c, r_start + r - 1 - (k - r - c))#3
    else:
        print(c_start + c - 2 - (k - 2*r - c), r_start + 1)#4
'''
1 : increase r
2 : increase c
3 : decrease r
4 : decrease c
'''