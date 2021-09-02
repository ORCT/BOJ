X = int(input())
check_num=1
n=0
while 1:
    if X == 1:
        print('1/1')
        break
    if X<=check_num:
        sum_row_col=n+2
        cal_num = check_num-X
        if n%2==0:
            row = 1
            column = sum_row_col - row
            row = row+cal_num
            column = column-cal_num
        else :
            column = 1
            row = sum_row_col - column
            row = row-cal_num
            column = column+cal_num
        print('{}/{}'.format(row,column))
        break
    n+=1
    check_num+=1+n