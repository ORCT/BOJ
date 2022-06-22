n,k = map(int, input().split())
num = [i for i in range(2,n+1)]
cnt = 0
while num:
    p = num[0]
    for i in num:
        if i%p == 0:
            num.remove(i)
            cnt += 1
            if cnt == k:
                print(i)
                break