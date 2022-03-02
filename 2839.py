N = int(input())
cnt = 0
while 1:
    if N==0:
        print(cnt)
        break
    elif N<3 and N!=0:
        print('-1')
        break
    elif N<13 and N%3==0:
        cnt += N//3
        print(cnt)
        break
    elif N<13 and N%3!=0:
        N-=5
        cnt+=1
    elif N>=13:
        N -= 5
        cnt+=1