n = int(input())
i=0
f=1
l=0 
while 1:
    f+=6*i
    l+=6*(i+1)
    if n==1:
        print(1)
        break
    elif n>=1+f and n<=1+l:
        print(2+i)
        break
    else:
        i+=1