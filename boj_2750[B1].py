N = int(input())
num_list=[]
while 1:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break
num_list.sort()

for i in range(len(num_list)):
    print(num_list[i])