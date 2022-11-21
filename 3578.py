h = int(input())
if h == 0:
    print(1)
elif h == 1:
    print(0)
elif h == 2:
    print(8)
elif h%2==1:
    print('4'+'8'*(h//2))
else:
    print('8'*(h//2))