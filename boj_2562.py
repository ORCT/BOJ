num_list =[]
for i in range(9):
    num = int(input())
    num_list.append(num)
    max_num_list=num_list
max_num_list=sorted(num_list)
for i in range(9):
    if num_list[i]==max_num_list[8]:
        print(max_num_list[8])
        print(i+1)