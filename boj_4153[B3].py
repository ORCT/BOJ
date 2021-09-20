while 1:
    num_list = list(map(int, input().split()))
    if sum(num_list)==0:
        break
    num_list.sort()
    if num_list[0]**2 + num_list[1]**2 == num_list[2]**2:
        print('right')
    else:
        print('wrong')