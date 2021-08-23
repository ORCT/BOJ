import sys
num_list=[]
while 1:
    try:
        num=int(sys.stdin.readline())
        num_list.append(num)
    except:
        break
div_num_list=[]
for i in range(len(num_list)):
    num = num_list[i]%42
    div_num_list.append(num)
div_num_list.sort()
count=0
for i in range(1,len(div_num_list)):
    if div_num_list[i]!=div_num_list[i-1]:
        count=count+1
print(count+1)