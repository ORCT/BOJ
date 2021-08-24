def find_hnum(n:int):
    check_num=int(str(n)[0])-int(str(n)[1])
    test_num=0
    for i in range(1,len(str(n))):
        cnt=0
        if int(str(n)[i-1])-int(str(n)[i])==check_num:
            test_num+=1
        else:
            test_num-=1
        if test_num==len(str(n))-1:
            cnt+=1
    return cnt

N=int(input())
if N<100:
    print(N)
else:
    cnt_num=0
    for i in range(100,N+1):
        plus_num=find_hnum(i)
        cnt_num+=plus_num
    print(99+cnt_num)