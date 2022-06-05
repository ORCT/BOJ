n,k = map(int, input().split())
c = [int(input()) for _ in range(n)]
c.append(100000001)
cnt = 0
while k != 0:
    for i in range(n+1):
        if c[i]<=k:
            continue
        else:
            cnt += k//c[i-1]
            k = k%c[i-1]
print(cnt)#인덱스때문임