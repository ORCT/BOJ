num = input()
first_num = num
count=0
while 1:
    num=str(int(num))
    count=count+1
    if int(num)<10:
        num = '0'+num
    cal_num=int(num[0])+int(num[1])
    if cal_num>=10:
        new_num=num[1]+str(cal_num%10)
    else:
        new_num=num[1]+str(cal_num)
    num=new_num
    if int(first_num)==int(new_num):
        print(count)
        break