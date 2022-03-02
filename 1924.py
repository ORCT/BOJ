m,d = map(int, input().split())
if m == 1:
    num = d
elif m == 2:
    num = 31+d
elif m == 3:
    num = 31+28+d
elif m == 4:
    num = 31+28+31+d
elif m == 5:
    num = 31+28+31+30+d
elif m == 6:
    num = 31+28+31+30+31+d
elif m == 7:
    num = 31+28+31+30+31+30+d
elif m == 8:
    num = 31+28+31+30+31+30+31+d
elif m == 9:
    num = 31+28+31+30+31+30+31+31+d
elif m == 10:
    num = 31+28+31+30+31+30+31+31+30+d
elif m == 11:
    num = 31+28+31+30+31+30+31+31+30+31+d
elif m == 12:
    num = 31+28+31+30+31+30+31+31+30+31+30+d
if num%7==1:
    print('MON')
if num%7==2:
    print('TUE')
if num%7==3:
    print('WED')
if num%7==4:
    print('THU')
if num%7==5:
    print('FRI')
if num%7==6:
    print('SAT')
if num%7==0:
    print('SUN')