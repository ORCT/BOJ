import sys
num_list=[]
while 1:
    try:
        num=int(sys.stdin.readline())
        num_list.append(num)
    except:
        break
num = num_list[0]*num_list[1]*num_list[2]
str_num= str(num)
for i in range(10):
    print(str_num.count(str(i)))